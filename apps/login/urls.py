# app level

from django.conf.urls import url
from . import views

def test(request):
	# naruto ascii
  # http://www.ascii-art.de/ascii/ab/anime.txt
	print """

                         ...                             |     |    |   |
    -`''-  _        ..########o...                       |     |    |   |
 _.'     `: \     ,##8#########8##o,,     (      (       `|    |    |   |
/ :  ___,-+-'   .#######8##8###8###8##,    )ailor )aturn  |    |    |   |
`-+-'     ;   ,#8###########8#8########,,                 `|   `|   |   `|
   `-...-'   :#88####8##8###########8###.,                 |    |  |'    |
            .HXX8X88X#8XX########XX8X8XX#;,                `|   |  |     |
           ,#O#X8888#88###########X####8X8,         _       `|  `\/'   ,/
          :8##88##X######8#8######X######8#:      _| |__     `|      ,/
         .######8##8####8)#)#(i#88####8####.:    |_   __|     `|    /
       .,#88##8#88###H8I~-_  _-~8+8##8####8#,:     | |___    __.----._
      :=#X##8#######,# ~-._()_.-~ ##########.,:    |  __ \   L__    __|
    .:I8##88####88#:;_--__    __--_,:#88#####),:   | |  \ |     |--|
   .:=8#XX#####88#LH =#O#\    /O##\i)##8######+:   | |  | \__  |'  `|
 .':###X888###8#8#O) \##@/    \##=/#H8###8####.,:  |_|  `\___| `|--|'
.':#####8####888L;;I,       |      #8###8##8###,.,              |  |
:.88Li######8#888#,H.     .__,    :8##88#####8##o:             |'  `|
:88X:##88##8##8#8##O8,           _8###########8#.8.           .|    |
8X#+#888#8##8#8#H.###8#,_      _-'8##=#####88#XX,o:           | \__/  _
X#..8#8##8##8888..8##8#8#-.__.-X#88##=8#####8#8#.,;           `.|__|-' |
'   HH8###;##8##,+888#L#|__  __|##88##;8###8##X'               ||(__- |'
_____                   |__()__|                _____          .|.:@#/_
\    `---.________.-----'      `-----._____.---'    /          ||._--' |
 \           oOOOOOOOOOOo__      ___oOOOOOOOOo    _/          | |(_----|
  \_.--_        oOOOOOOOOo -   --   oOOOOOOo __.-'            | |(_--__)
 _-:_-'           oOOOOOOOo        oOOOOOOo    `-_            | |.:(__ )
<::<_      _        oOOOOOOo       oOOOOo |       -_          `||.:@#_/
 ~-_:-__.-':'      xXXXxoOOOo ,|, oOOOoxXXXx _______\         |||.:@#|
    -_|    |        xXXXXXXXXx\|/.xXXXXXXXx  \ \             / `|.:@#|
      |   |'   _-.  xXXXXXxx--=O=--xxXXXXx|___| \           /  .|.:@#|
      |   |__-':/    xXXxxXXx'/|\`.XXxxxXX:.  '  \        ./  .:|.:@#|
      |     :::||    xxxXXXXx.'|`.xXXXXXxxx::.    \      /   .::|.:@#|
      |     :::||_  xxXXXXXXXx/'\_xXXXXXXXXx::.    \    /   .::/|.:@#|
      |    :::|' \`--xXXXXXXXx     xXXXXXx  \::.    \  /   .::/ |.:@#|
      |    :::|   \   xXXXXXX      xXXXx     \::.   /\/   .::/  |.:@#|
      |    ::|xx   \    xXx         xx        \::. /oO|  .::/   |.:@#|
     |'   .::|XXXXxx|    `          '|   xxxxx \::/OoOO\.::/    |.:@#|
     |    ::|XXXXXXX|                |xXXXXXx   \|oOOooOOOOo    |.:@#|
 ,-__|__ .::|XXXXXX/__              |_XXXXXx      OoooOoooooo   |.:@#|
 \ooooOOo::|XXXXXX/__ \,            | \XXXx       oOOOooOOOO    |.:@#|
  \OOOoooooo|XxoOOOo.\. \          / ./oOOoXXXXXx   oOOOoooo    |.:@#|
   |OOOOOOOO|oOOOOOOOo.\ \,       / /oOOOOOOoXXx       oOOo.    |.:@#|
   |oooooooo|OOOOOOOOOOo.\ \     / /oOOOOOOOOOOOo [ -Tim Park ] |.:@#|


REGister worked ?????!!!!!!
	"""

urlpatterns = [ 
    url(r'^signin$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),  
]
