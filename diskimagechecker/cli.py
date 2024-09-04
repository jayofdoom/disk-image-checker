# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
import os

import click
from oslo_utils.imageutils import format_inspector

@click.command()
@click.option('-v', '--verbose', 'verbose', help='Verbose output',
              is_flag=True, default=False)
@click.option('-i', '--image', 'image', help='Image to inspect',
              required=True, type=str)
def main(image, verbose):  # pragma: no cover
    if not os.path.exists(image) or not os.path.isfile(image):
        click.echo('Image path %s provided does not exist' % image, err=True)

    inspector = format_inspector.detect_file_format(image)
    safe = True
    try:
        inspector.safety_check()
    except format_inspector.SafetyCheckFailed:
        safe = False

    virtual_size = inspector.virtual_size
    actual_size = inspector.actual_size
    fmt = str(inspector)

    if verbose:
        click.echo('SAFETY_CHECK_PASSED=%s' % safe)
        click.echo('VIRTUAL_SIZE=%s' % virtual_size)
        click.echo('ACTUAL_SIZE=%s' % actual_size)
        click.echo('IMAGE_FORMAT=%s' % fmt)

