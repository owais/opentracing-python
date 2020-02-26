# Copyright (c) The OpenTracing Authors.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import sys

from tornado import version_info as tornado_version

if tornado_version < (6, 0, 0, 0):
    print("using tornado context stack")
    from ._tornado import TornadoScopeManager, tracer_stack_context
else:
    def tracer_stack_context():
        return _NoopContextManager()

    if sys.version_info >= (3, 7):
        print("using contextvars")
        from opentracing.scope_managers.contextvars import ContextVarsScopeManager as TornadoScopeManager
    elif sys.version_info >= (3, 0):
        print("using asyncio")
        from opentracing.scope_managers.asyncio import AsyncioScopeManager as TornadoScopeManager


class _NoopContextManager(object):
    def __enter__(self):
        pass

    def __exit__(self, *_):
        pass

