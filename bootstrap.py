#!/usr/bin/env python

import argparse
import logging
import os
import shutil

LOG = logging.getLogger(__file__)
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())

# TODO consider alternative: appending .symlink to filenames
NOT_DOTFILES = ['README.md', 'bootstrap.py', '.git', '.gitkeep']


def files(path):
    result = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)) \
                and (file not in NOT_DOTFILES):
            result.append(file)
    return result


def safe_needs_symlink(relative_target, link):
    """
    returns true if symlink still needs to be set up, false if it already works
    """
    if not os.path.exists(link):
        LOG.info('\t[ok] dest file doesnt exist: {f}'.format(f=link))
        return True
    LOG.info('\tdest file exists: {f}'.format(f=link))

    target = os.path.abspath(relative_target)
    if os.path.islink(link):
        LOG.info('\tdest file is symlink: {f}'.format(f=link))
        old_link_target = os.path.abspath(os.readlink(link))
        LOG.info('\told target={o} new_target={n}'.format(o=old_link_target,
                                                          n=target))
        # note: important that both paths have been canonicalized
        if target == old_link_target:
            LOG.info('\t[ok] link already points to {t}'.format(t=target))
            return False
    else:
        LOG.info('\tdest file not symlink: {f}'.format(f=link))

    bakfile = link + '.bak'
    LOG.info('\tcopying {s} to {d}'.format(s=link, d=bakfile))
    shutil.copyfile(link, bakfile)
    LOG.info('\tdeleting {s}'.format(s=link))
    os.remove(link)
    return True


def bootstrap_dotfiles(os_type, profile=None):
    assert os_type
    LOG.info('running with os={o}, profile={p}'.format(o=os_type, p=profile))

    dotfiles_dir = os.getcwd()
    home_dir = os.path.expanduser('~')
    LOG.info('dotfiles_dir=[{d}], home_dir=[{h}]'
             .format(d=dotfiles_dir, h=home_dir))

    dotfiles_env_fname = os.path.join(home_dir, '.dotfiles_env')
    if not os.path.exists(dotfiles_env_fname):
        # write a .dotfiles_env file
        LOG.info('{f} not found; creating'.format(f=dotfiles_env_fname))
        with open(dotfiles_env_fname, 'w') as outfile:
            outfile.write(""" #!/bin/bash
export DOTFILES_OS={o}
export DOTFILES_PROFILE={p}
""".format(o=os_type, p=profile))

    # symlink over the common/root dotfiles
    common_dotfiles = files(dotfiles_dir)
    for fname in common_dotfiles:
        abs_real = os.path.join(dotfiles_dir, fname)
        abs_link = os.path.join(home_dir, fname)
        LOG.info('found:  {l} -> {r}'.format(l=abs_link, r=abs_real))
        if safe_needs_symlink(abs_real, abs_link):
            assert not os.path.exists(abs_link), \
                    'link_name should have been backed up and rm-ed'
            os.symlink(abs_real, abs_link)
            LOG.info('created link:  {l} -> {r}'
                     .format(l=abs_link, r=abs_real))

    LOG.info('======== STARTING OS-SPECIFIC DOTFILES =========')
    os_dir = os.path.join(dotfiles_dir, '__%s__' % os_type)
    os_dotfiles = files(os_dir)
    for fname in os_dotfiles:
        if fname in common_dotfiles:
            raise ValueError('conflict between os-specific dotfiles')
        abs_real = os.path.join(os_dir, fname)
        abs_link = os.path.join(home_dir, fname)
        LOG.info('found:  {l} -> {r}'.format(l=abs_link, r=abs_real))
        if safe_needs_symlink(abs_real, abs_link):
            assert not os.path.exists(abs_link), \
                    'link_name should have been backed up and rm-ed'
            os.symlink(abs_real, abs_link)
            LOG.info('created link:  {l} -> {r}'
                     .format(l=abs_link, r=abs_real))

    if not profile:
        LOG.info('No profile provided; done.')
        return

    LOG.info('======== STARTING PROFILE-SPECIFIC DOTFILES =========')
    profile_dir = os.path.join(dotfiles_dir, '__%s__' % profile)
    profile_dotfiles = files(profile_dir)
    for fname in profile_dotfiles:
        if fname in common_dotfiles:
            raise ValueError('conflict between profile-specific dotfiles')
        abs_real = os.path.join(profile_dir, fname)
        abs_link = os.path.join(home_dir, fname)
        LOG.info('found:  {l} -> {r}'.format(l=abs_link, r=abs_real))
        if safe_needs_symlink(abs_real, abs_link):
            assert not os.path.exists(abs_link), \
                    'link_name should have been backed up and rm-ed'
            os.symlink(abs_real, abs_link)
            LOG.info('created link:  {l} -> {r}'
                     .format(l=abs_link, r=abs_real))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--os')
    parser.add_argument('--profile')
    args = parser.parse_args()
    bootstrap_dotfiles(os_type=args.os, profile=args.profile)


if __name__ == '__main__':
    main()
