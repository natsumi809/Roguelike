import time

def orenokati_game():
    naguru_art = """
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<:<<<;;>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;<<<~___````___~<<??>??>??><<<<<:;;;;;;;;;;;;;;;;;;;;;;;;;;;
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><~__````` ````` `~<<<;;;<<<~_._~__~<;;>??????????????????>?
????????????????????????????????????????<~`````           ````___.....```..__~:;>???????????????????
?????????????????????????z<<<<<<<<>><<<!_`````  `        ` ```.....`````````.~_(;>???????????????=?=
======================z<<<~~___~~____`.``````            ```````````` `   ```.._(;>=================
=====================<<<__``` ` ````````````  `      `      ``````` `     ````.._:>?=l=l=l=l=l=l====
l=ll=ll=ll=ll=ll=llz<<__````      ` ``````                   `` ``     `   ```..~:;>?ll==l==l=l=ll=l
============z<<<<<<<_.````                               `                ` ```.~~;>?=l=?==?=?=?=?==
?????????<<~~~___`.`````                                    `          `   ````..~:;?==?????????????
>>>>>>><<__. ``````````   `                        `  `   `  ` `         `  ```..~:;?==?>>>>>>>>>>>>
>>>>>><~_``````` ` ` `            `  `          `      ` ` `` `         ` ` ```..~;;>?=<>>>>>>>>;>>;
;;>;;;<_```             `           `          `   `  `  ```````  `  `     ````..~:;>==<;;;;;;;;;;;;
;;;;;<_ `   `  `                `  ` `` `         `  `` ``````. `      ` `` ```..~:;??l<;;;;;;;;;;;;
;;;;;<_      `   `  `             ` ```      `     ` ` `````..._`         ` ```..~:;>?=z;;;;;;;;;;;;
;;;;;<_`  `      `             `  `````` `      `   ` `````..~__``  ` `  ` ````.~~:;>?=z;:;;;;;;;;;;
;;;;:~ `       ` ``         `   `  ``- ``        ` ` ``````..~:<-`     ` `````...~:;>?lz::;:;:;:;;:;
;:;:;_`     `   ``` `        `  ````.__`    `  `  ` ` ````..~::<_`   `   ` ````.~~:;>?=z;:;;:;;;:;;:
;;;;:_``     `  ````     `    ` ````.__```         ` `````..~~:<_``   ` ` ````...~:;>?=z;:;;;;;;;;;;
;:;;:_``  `   ``` ```      `  `` ```-(_``     ` ` ` ``````..~::;_` `   ` `````..~~:;>?=z;:::;:;:;:;;
;;:;<_``       `` _```  `   `  ````..(<.``       ` ` `````..~::;_``  ` ``````....~:;>?=z:~~:;;:;;;:;
;;:;<_`     ` ```__.`       `` ````._(<_``  `  `  ` ``````..~::;_.`   `  `````...~:;>?=z<~~~:;;:;:;:
:;;::_``  `   ```___``    `  ``````.~:<_``      ` ```````...~:;><-`    ``````...~~:;>?=z<~._(:;;:;;;
;;;;:_``     ` ``_<_``        ` ```.~(>_.`    `  `  `````..~~:;><_`  ` ` ````....~:;>?=z<_.._:;;;:;;
;:;;;_``   `  ```_:_``  `  ` `````..~(?<.`  `    ` `````...~~;>?<_`   ` ``````...~:;;?=z<_..__;;:;;:
;;;:;_ `     ````_(_.`      `  ````..(+<.`     ` ```````..~~:;??<_ ` ` ` ````....~:;;?==<_`.._(;;;;;
;;;;;<_`    `  ``_(<.``   `  ``````.._<<.``  `  `  ````...~:;>?=<_``  ` `````...~~:;>?=z<_.`..~;;;;;
;;;;;<_  ` `` ``._(<_ `      ` ````.~_<=_.`   ` ``````....~:;>?=<_ `````````....~~:;>?=z<_.`.._;;;;;
;;;;;;_-```````.._(?< `  ` `` ````...~<1:_```` ``````...~~::;>=l<__``````.....~~~:;>>=lz<_.`.._;;;;;
>>>>>><__-...-___(<+>_ `` ```````...~_;+z_-```````....~~~::;>?=lz<__....._~_~::::;>>=zl<<....~(;;>>;
;;;;;><<;_::::::;;>1O__````````....__:;+O<__......_~~::::;;>?=zOz<<__~~:::::;;;;;>?=llz<~...._(;;;;>
;;;;;;;<<>>;;>>>>?=lwo__-...-__~~_::;;>1zO(__~~~__::::;;;>??=zw0z>;;;;;;;;;;>>>>?==ltz<<~...~(<;;;;;
;;;;;;;;;;;;;;;;;>;;>1c<____:::::;;;>>?=OXs<;;;;:;;;;>>>??=lztOzzOz++>>>>>>????1zztvz<<~~..~_<;;;;;;
;;>;;;;;;;;>;;>;;;;;;;zz<;;;;;;>>>>??==zwUW0+>>;>>>>>???1zzOvz<;<+1zzOtttttttOOOz1<<;<~~.~~_:>>;>;>;
>;>>;>>>>;>;>>;>>>>>;>;<<1<>>>>???????11111111?1wwwwOrrOOI1<<;:::;;;>>>????>?>><;;:::~~~~_(<>>;>>>;>
>;>;>>;>;>>;>;>;>;>;>>;>;>;;>;;;;;>;>;>;;>;;>>+OOOzz111?>>;;::::::::;;;;:;;;;:;:::::~~~:::<>;;;;;;;;
>>>>>>>>>>>>>>>>>>>>>>>>>>?>>>?>>>>>>>>>>>>>>>1z=?>>>>;;;;;:;::::::::::::::::;:::::::::;;+z>?>>?>>?>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>+lz??>>;;>;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;>?1z>>>>>>>>;>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>?>>>>>1Oz???>?>>?>>?>?>>>>>>>>>>>>>>>>>>>>>>??1l<>>>>>>;>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>zttlzzzzlzlllllllllllzz=====?=???===zztz+?>?>>?>?>?>?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<;<<<<<<<><<<111zzzzllllOvz1>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""

    tsuku_art = '''
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMHHMMMMMMMMMMMMMMMMMMMMMMMMMBTYTTUUUUUUUUUUUUUUUUUUUUUUUUUU
zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz<!`  ` `~<;;;;;;;;;;;;;;;;;;i<~ ` `  _1========================
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO<``       _<????????????????zv``      ` <rrrrrrrrrrrrrrrrrrrrrrr
rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrOZ~`         _ztlttlttlttlttllv_        ` (zrrrrrrrrrrrrrrrrrrrrrr
rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrI_ ` ` ` ` ` (OrrrrrrrrrrrrrO<_` ` ` `   (zzvvvvvvvvvvvvvvvvvvvvv
VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVI<_`  `     `(OuuuuuuuuuuuuuI< `    `  ` (vOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOz_ `   `  `` jzvvvvvvvvvvvZ<~`  `    ``.+vzzzzzzzzzzzzzzzzzzzzzv
rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrO<_`` `  `   (zlllllllllllv<_``   ` `` (zwwwwwwwwwwwwwwwwwwwwwww
VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVwz_ `      ``_+tttttttttttv<_` `   ` `.(rrrrrrrrrrrrrrrrrrrrrrrr
zuzuzuzuzuzuzuzuzuzuzuzuzuzuzuzuzzuzwz<_`` `  ` ` (OvvvvvvvvvZ<~ `  `   ` _juuuuuuuuuuuuuuuuuuuuuuuu
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOI<_ ``       _jvvvvvvvvvZ<_``    ` ` (ttttttttttttttttttttttttt
zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzuzwz<_`` `  ` ` (OOOOOOOOwI<_`  `   ``-+zzzzzzzzzzzzzzzzzzzzzzzzz
rtrrrtrrtrtrtrtrtrtrtrtrtrtrtrtrrtrtrtO<__`` `  `` _jtrttttrO>~``    ` `._jOOOOOOOOOOOOOOOOOOOOOOOOO
uZuuuZuuZuZuZuZuZuZuZuZuZuZuZuZuuZuuZZXz<_```     ` <wzuuzuzI<_`` `  ``` (Z0000000000000000000000000
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO<__`` `   ` _zrrrrrvI<_``     ``_jwwwwwwwwwwwwwwwwwwwwwwwwww
zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzwz<__```  ` `-(zlllzt<~_`  `  `` _zOOOOOOOOOOOOOOOOOOOOOOOOOO
rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrttOz<_-``  ` ``_+===zv<_.`  ` ``` (wrrrvrrrrrrrrrrrrrrrrrrrrrr
rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrOI<<<~~<?1z<_.``   ``-(=llv<~_```    ``_+wrrrrrrrrrrrrrrrrrrrrrrrrrr
tttttttttttttttttttlvz1zOOttttZz<_..``.`._~><_.``   ` _jvZ<<_.``   ` ` _jOOOOOOOOOOOOOOOOOOOOOOOOOOO
vvvvvvvvvvvvvvvvvZC>~__``__<zX0<_.````````.(<_.``  `  -(zI<~_.``  ` `` (zwwwwwwwwwwwwwwwwwwwwwwwwwww
UUUUUUUUUUUUUUUUVC<_.``` ```_?S>_````  ````_+<.``    ``___`````     ``-(ttrtrtrtrttrttrttrttrttrttrt
wwwwwwwwwwwwwwwwz<_```   ``` _zz_``  `   ``_+c_``  `  ````````  `  ```_(uuuuuuuuuuuuuuuuuuuuuuuuuuuu
XXXXXXXXXXXXXXXXv<_`    `  ``_jI_``   ` ```-<I_`  `   ` ````   `  ```._<vvvvvvvvvvvvvvvvvvvvvvvvvvvv
vvvvvvvvvvvvvvvvz< ``  `    ` (I_`` `    `` (z~`   `          `   ````_(OOOOOOOOOOOOOOOOOOOOOOOOOOOO
?=?=?=?=?=?=?=??z<``  `   ` ``(O_  ` ` ` `` _<_` `  `  `    `   ` ```._(????????????????????????????
================O<   ` ```   -(r<-       .___<_   ``      `  ` `````..~(+zzzzzzzzzzzzzzzzzzzzzzzzzzz
ttttttttttttttttwc_~~_--.-_~~_(w<~~__:~~~<<<<<<~~________~~~_.  ````..._+OOOOOOOOOOOOOOOOOOOOOOOOOOO
llllllllllllllllWI<_:~~:~~:::;jZI_:<<_`     `  `     `   ` `  `_.-.`..._jttttttttttttttttttttttttttt
pppppppppppppppp0z1z+<;;::;;+zZz1z+z<-```        `  `  `      ` ` __~--~+UUUUUUUUUUUUUUUUUUUUUUUUUUU
OOOOOOOOOOOOOOOOO<<1OwzzzzzzZ>~__jwX+_ ```     ```    ``` `  `   ` ` __<<lllllllllllllllllllllllllll
llllllllllllllllz<::<<<?<<<<_...~(?XX<__.~~~~~.........-```    `    ` ` _<1lllllllllllllllllllllllll
rrrrrrrrrrrrrrrrv<~~~~~~~......~~~:<+1+<_:~~~~~~~~~_:~~~.````   ` `    `` (jwwwwwwwwwwwwwwwwwwwwwwww
ttttttttttttttltO<~~............~~~::<1Ow&+++<(+<<+<<::~~..``` `   ` ` ```_(zlltlltlltlltlltlltlltll
=?=?=?=?=?=?=====>:~.~...........~~~~:<+OXuXyyyVWfppWmo<_~..```  `  ` ````-(+zzzzzzzzzzzzzzzzzzzzzzz
ltltltltltlllllltI_~......`````...~~~~::<+zOOZZXX00UXWWWo_~.````  `  ` ``..(+ltttttttttttttttttttttt
lltlltlltlttltlttz<_....```   ````._.~_~~:;<<<<<+<+1zOZX0>_.```  `  ` ```._(+OOOOOOOOOOOOOOOOOOOOOOO
ZZZZZZZZZZZZZZZZZI<_...```  `   `````...~~~~::~::::<;<<+1<~.```   ` `````-_<zOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOz_~.`````  `   ` `````.....~..~.~~~~~~~<_.````` ``````._(+wwwwwwwwwwwwwwwwwwwwwwww
uuuZuuuZuuuZuuuZuuI<_..`````` `   ` ```````.....`..........````` ``````.__<zXuZZZuZZZuZZZuZZZuZZZuZZ
VVVVVVVVVVVVVVVVVVkz_~.````` ` ``     ` `````````````......``````````..__(+dUUUUUUUUUUUUUUUUUUUUUUUU
ZZZZZZZZZZZZZZZZZZXI<__..`````` `` `   ` ` ```````````..`.`````````..._~(+dZZZZZZZZZZZZZZZZZZZZZZZZZ
0000000000000000000Xz<__.`````` ` ` ``    `  ` `````````.``..``.`...~~:<+zzzzvvvvvvvvvvvvvvvvvvvvvvz
wwwwwwwwwwwwwwwwwwwwO+<__..``````` `` ` `   ` ` ``````.``........~~~::<+zwXXXXXXXXXXXXXXXXXXXXXXXXXX
vvvvvvvvvvvvvvvvvvvvwO+<__..```````` ```` `` `` ``````.........~~~::;;+zwwwwwwwwwwwwwwwwwwwwwwwwwwww
ZZZZZZZZZZZZZZZZZZZZZXyz<___...```````` `` `` ```````.`.....~~~::::;>1zXUUUUUUUUUUUUUUUUUUUUUUUUUUUU
zuzuzuzuzuzuzuzuzuzzuzzwz+<___...```````````````````......~~~:::;;>+zwzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
vvvvvvvvvvvvvvvvvvvvvvvvvOz+<____~...``````````````.....~~~:::;;>+zOzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
uuuuuuuuuuuuuuuuuuuuuuuuuuuwzz+<<_____.....````.`....~__::;;;>?1zzzuzuuzuuzuuzuuzuuzuuzuuzuuzuuzuuzu
vvvvvvvvvvvvvvvvvvvvvvvvvvvvwzwOz++<<________________(+<<>??1zzwwXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
fpffffffffffffffffpffpffpffpfpppWAwzzz1+++++<<<<+++++11zzzzwwXWppppppppppppppppppppppppppppppppppppp
ffffffffffffffffffffffffffffffffffffWXXAwwwwwwwwwwwwwwwkXWVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
'''

    hippataku_art = '''                         
                                       .(;;;;;<-.     
                                       (z>>>>>>>?+.         
                   .(<<;;<-.          -Oz?>>>>?<1z>`    
                  (=z???>>+=<         dwz=??>>??zwk.           .----. 
                 .wOl=?????=O<`      .XXO=?????=zwX_         (zz>>>>zO+  
                 (Wwl==?>>?=Ok_      .fXOl=???=lOuW;        (V1<>>>+lwX;
                 (WuOll=???=OXl      .pXtt==?==lwuW{       .0I=>>>??zwXP  
                 -WXwll=???=twS_     .pXtl=====lwuW{       dwz=???=zwXWD   
                  WfXtll?===lwW;`    -WuOl=???=lwuW}      (Wtl==??zOwXW$
                  dHuOtl====lOX$     (HZOl==??llwZW}      dXtl====twXWH}
   .(<<?1-        (HZwrl=???=OXW.    (HXtl===?llwZW}     .XZOl=?=lOwXWK_     
 .dwOz>>+zO-      .HkXrl===?=twW;    (HXOt====llwXW}     (SZO===llwXfWD`  
 .kkwz=??1OX-      WHkwtl==?=twXr    (WZwl====llwXWr     dXtIl==llwZWH>
 .kWXwOlz?1wG-     qHXwtl===zltwW.   (HZwll===llwXWr    .Wwtl===lOwXWK`
  WHWXwtl=zldI     ,HWXOll==zlOuW{   (HZwtl==lltwXWr    jSOt====twXWHt`
  (HWWXwtlllOX;     HkXwtl==lltwX$   (HZwtllllltwXWr   .XXtll=llOwXWH:
   dHWXzrl=llwX-    dHkzOll==ltrXR.  (HZztll=lltwyWr   (Wztll==twZWHD 
   .HHWuztl=lOwn.   (HWurtl=l=lrXW;  (HyzttlllltwyWr   d0Olll=ltwZWH\ 
    ?HHyXwtlllOXl   .HHXrttl=llrwXr  (HyztllllltwyWr  .WXtlll=lrXXW#  
     UHWXXrt=lOwS-   dHXzrtlllltzXR  (HyXrtllltrwyWr  JWXtll=ltvZWH%
     .HHWXwtlllwXn.  JNkkrtll=ltwZW_ (HyXttlllttwyWr .X0OtllllOzXWH! 
      ?HHWXvtlllwXl  .MWXvtlOlltrXWr`(HXwrtlllttwXW$ (SZOlllltwufWP   
       WHWXurll=zwU+ .WHXvtlz==zz1z1(zz1<<<>>><<<<<1(zz11ll=ltwufH}
       .MHWuwtl=??1O+.d0C1<<>;;;;;;:;;;;;;;;;;;;;;;;;;;;>;;>+1OXWK~ 
        ?HWXzt==?>+<<<><<;;;;>;;;;;;;;;>>>>>>>>>>;>>>>>>>>>>>+zwW$` 
         UHWwO=?>;;>;>;;;>>>>>>>>>????????????????>??>??????zzwub{`
         .HkkOzz??>>>??????>?????=======================zlzzzwwXK`
          jHWXwOzz===?=======lllllllllllllllllllllllllttttrrwuXyH                .._(::;::;<-.   
           WHyuzrtllll=lllllttttttrrrrrrrrrrrrrrrrrrrrrrrrzuuuyVH.             .(;;;;;;;;;<>++zz. 
          `jHWZuvrtttlltttttrrrrvvvvzzzuuuuuuuuuuuuuuuzzuzzuuuyyW_          .(;;;;>>>>???zzzzOwww+
           ,qfyZzvrrttttttrrrrvzzuzuuuuuuuuuuuuuuuzuzzuuzuzXXXUUW_        .(;;>>>???=zlOwwXXXXWWWR_`
           .qpyZuzvrrttttrrrrvvzzuuuzuzzzzzzzzzzzzvvvwwOOzz111zzOl      .+<>????==zzwwXXXWWWHmH@H=``
            WpfyuuvvrtttttrrrrvzvvvvrrvvvvvvvvrrrrOOz1???>>>>>>>+<<-.-(;>>???==zOwwXXWpWkHmHHHY!`
            dHfVZurrttttttttttrttttttlttttttttrtlz<>>>?>>>?>>>>><;;<;;;>>??=ltwwXXWWkqqg@HY=! `   
            JHpWXuvrtlllllllllllllllllllllltllz1>>;>>>>>>?>?>>>>>>>>>>???zzzwwXXWWkqHHMY!``
            .mHpZuzrttllllll=lllll=lllllllll=?>>>>>>>??>???????>????===ltrwXXfpWqmH#Y!``  
             WHHVXuzrtll====================?>>>>>?>>????=??=?====llttOwwXXWWWHHH9!``
             JHqpWZuvttll====???????=??===z>>>?>?????=====llllllttrwzwuXXWWWqHHY``         
             .MHHpWXuwrtllll====?==?=?=??????????=====llllltttrrrzwwXXVpWHqHM=`
              zMHkWWZXwrrtlll==l===========??===ll=llllttrrrvvzuuZXXWWkHmHHY``
               WMgHWWWXXvrrtttllllllll=llllltlttttttrrrwzzzuuuZyVWWWkmgHMY`` 
               .HMHqbWWXuuzzrrrtrttttttlttOrrvrvvzzzuuuuZZZyWfpppWmHHHHY`
                .WMHHHHWWWXZXuzzzzvvvrrvzzuuuuZZZZyyyyyVffppWkqqmg@MMY`
                  ?MMHHgmkWpWyXXZZuuuuuuZZXyVVffffffpppbkkkqHqH@HM#=  
                    TMN@H@HqHHbWpWpfWWVWWWWkWWHqqqqqqqmmmmggHHMMY!`  
                      ?TMM@@ggggmmmmmmqmmmggggggggmgg@ggHHMMM9!
                         ?TBMHMM@@@@@@@@@@@@@@@@@@@@@HMMMB=!``
                           `` _?7""YWMMMMMMMMMMMMMB9"=! ``
'''


    teki_hand = (input("じゃんけんしよう！グー・チョキ・パー、どれを出す？→"))

    print("ジャン、")
    time.sleep(0.7)
    print("ケン、")
    time.sleep(0.7)
    print("ポン！")
    time.sleep(0.7)


    if teki_hand == "グー":
        god_hand = "パー 🖐️"
        print(hippataku_art)
        time.sleep(2.5)
        print("私の手は", god_hand)
        time.sleep(1.3)
        print("私の勝ちです。😁")
        time.sleep(1.3)



    elif teki_hand == "チョキ":
        god_hand = "グー 👊"
        print(naguru_art)
        time.sleep(2.5)
        print("私の手は", god_hand)
        time.sleep(1.3)
        print("私の勝ちです。😁")
        time.sleep(1.3)



    elif teki_hand == "パー":
        god_hand = "チョキ ✌️"
        print(tsuku_art)
        time.sleep(2.5)
        print("私の手は", god_hand)
        time.sleep(1.3)
        print("私の勝ちです。😁")
        time.sleep(1.3)



    else:
        print("何それ？")

orenokati_game()