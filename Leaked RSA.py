from cmath import sqrt
from Crypto.Util.number import *
from sympy import mod_inverse


p = getPrime(512)
q = getPrime(512)

e = 65537

while p<q:
    q=getPrime(512)

n = p*q

eq = (n**3)*(5*(p+1)**2 + pow(p,4)) + 5*n*(q+p) + q**2

#flag_num = bytes_to_long(flag)


#c = pow(flag_num, e, n)

"""with open('output.txt', 'w') as f:
    f.write(f"{n =}\n{c =}\n{e =}\n{eq =}")
"""    
n =125205720235096866603271200818101064201421456743237916735390028589031734473242408432442090587932616788909482626308003018291297082250486407968637571380808160865667665875589066465082225130393512184417692553908579478873744862501194249123931208439641299662606998130361485579205103915017892972430466648748563499957
c =101807361318778273098628734716889883517784208660729303769852883609943969831072956946516106170955725739335293782773462652766290651917913710630953541338956727623357387170063342663242088610001887992062565753747240706267842191227021662996992967271989387268633762613569835271673021028428284256710585696977346490577
e =65537
eq =40890929899318362923179881188467879553031102942906748834246077162986227542134681885734037800576905168848161867742195749717863316520265188323397612874520068979335178695108639975968896785497049813733871395155222995881530458832027590966527437031882321915851935427955121807710550204990614781436044586609993937608656466966077199619416080075211982345954790271390116826404974328053838806573075961148639385865637151711515519924645698148318060155556106021200142747886329497548933066437763499129556320453315842412186732970997919990985777368465707314173278805436337489180811676652933819376175274570958795066028534869552608048922528219377127198126578705301316490361826932832671038409803009984422693255875307815703505272991364243077861043531946386878432780466073152236375940559045943848301151310804037317086954150364907339380809145039314969715776754255985027159095635386487026964910884444009615842904651840783042645115140250275004800366771008610710305794481586437526603254441296392098734019197677222580253681292054847635408771269201442883989385312177409683066427397087397966020213103253734184901191760023798501855335101451287011386400092552409455589353621283672273634136577077428587480899023040945484147570428498140757406132974396149040428770115388216015014788334073684331706931457849869189141830451706688829374521721743544565334204063064918512142937906559427850486248340727798313076035959711395212759618457319839082576675213066912868779553844971380993347874848677561605787448335468227589666386127972404912313567867187799739287970944827477917679371389312

q2=108610322771696137617937083406677160403343082336712687265273466262676355869227604320298628404083932277711074477813810273740430756684709641659344117803493888771764146497532979296043713106635925791557307380362366355091439736569925217233402690247568140281363573018333225848336120577555656656806073457730649094489

q=10421627645032043535601489848589928030188724910051719938991636837913614048742156162396264683151575443886658683304310827031077299943994513972420061809135067
p=12014027414881017339214788832289382822025840812317273596382674485541072731280020834591678769789299878032870521358451373242577436912372774943481675929610671


print(p*q==n)
d=mod_inverse(e,(p-1)*(q-1))
m=pow(c,d,n)
print(long_to_bytes(m))
