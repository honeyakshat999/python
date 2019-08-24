% irb
> require 'base64' ; require 'uri'
 => true
> Base64.decode64(URI.decode("pfhu5exu9jirgp6ZLAhM2g%3D%3D"))
 => "9\x1Far\x9D|\xF8-[\n\x12\xB5\xD0\xD9QF"
