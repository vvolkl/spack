# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import pytest

import spack.environment as ev
from spack.main import SpackCommand, SpackCommandError

# everything here uses the mock_env_path
pytestmark = pytest.mark.usefixtures(
    "mutable_mock_env_path", "config", "mutable_mock_repo"
)


@pytest.mark.disable_clean_stage_check
def test_fetch_in_env(
    tmpdir, mock_archive, mock_stage, mock_fetch, install_mockery
):
    SpackCommand("env")("create", "test")
    with ev.read("test"):
        SpackCommand("add")("python")
        with pytest.raises(SpackCommandError):
            SpackCommand("fetch")()
        SpackCommand("concretize")()
        SpackCommand("fetch")()


@pytest.mark.disable_clean_stage_check
def test_fetch_single_spec(
    tmpdir, mock_archive, mock_stage, mock_fetch, install_mockery
):
    SpackCommand("fetch")("mpileaks")


@pytest.mark.disable_clean_stage_check
def test_fetch_multiple_specs(
    tmpdir, mock_archive, mock_stage, mock_fetch, install_mockery
):
    SpackCommand("fetch")("mpileaks", "gcc@10.2.0", "python")


def test_fetch_no_argument():
    with pytest.raises(SpackCommandError):
        SpackCommand("fetch")()

versions = SpackCommand('fetch')


@pytest.mark.network
@pytest.mark.usefixtures('mock_packages')
def test_fetch_commit_extrapolation():
    """Test the git commit extrapolation of a version."""

    versions('--no-checksum', 'brillig@commit.e03d9f58a')
