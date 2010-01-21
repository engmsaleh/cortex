##########################################################################
#
#  Copyright (c) 2009, Image Engine Design Inc. All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#
#     * Neither the name of Image Engine Design nor the names of any
#       other contributors to this software may be used to endorse or
#       promote products derived from this software without specific prior
#       written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
#  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
#  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
##########################################################################

import unittest
import IECore

class SubstitutedDictTest( unittest.TestCase ) :

	def test( self ) :
	
		d = {
			"a" : "hello ${name}",
			"b" : IECore.CompoundObject(
				{
					"c" : IECore.StringData( "goodbye ${place}" )
				}
			)
		}
		
		ds = IECore.SubstitutedDict( d, { "name" : "john", "place" : "london" } )
		
		self.assertEqual( ds["a"], "hello john" )
		self.assertEqual( ds["b"]["c"], IECore.StringData( "goodbye london" ) )
		self.failUnless( isinstance( ds["b"], IECore.SubstitutedDict ) )
		self.assertEqual( ds.get( "a" ), "hello john" )
		self.assertEqual( ds.get( "notThere" ), None )
		self.assertEqual( ds.get( "notThere", 10 ), 10 )
		self.assertEqual( ds.get( "a", substituted=False ), "hello ${name}" )
		self.assertEqual( ds.get( "b", substituted=False )["c"], IECore.StringData( "goodbye ${place}" ) )
		self.failUnless( ds.get( "b", substituted=False ).isInstanceOf( IECore.CompoundObject.staticTypeId() ) )
		self.assertEqual( ds.get( "notThere", substituted=False ), None )
		
if __name__ == "__main__":
    unittest.main()
