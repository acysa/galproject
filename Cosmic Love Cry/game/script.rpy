# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define L = Character("伊瞳",image = 'char/lyt normal.png')
define H = Character("经芷",image = 'char/htt normal.png')
define interviewer = Character('面试官',image = 'char/other/interviewer.png')
define B = Character('顾芯', image = 'char/hl/hl normal.png')
define LQ = Character('十日十乞十八子', image = 'char/other/lq normal.png')
define F = Character('Felix', image = 'char/other/felix half front1.png')
#声明游戏变量
#好感度
default H_point = 60
default L_point = 60
default B_point = 40
default LQ_point = 20
default F_point = 10

#分支控制
#回家意愿
default route_home = False
default present_1 = False
#日记页数
default page_num=0
#声明游戏资源
#背景
image bg room = "bg/room.png"
image bg street ="bg/street.png"
image bg street_night ="bg/street night.png"
image bg dream ="bg/dream.png"
image bg bad_dream ="bg/bad_dream.png"
image bg dream1 ="bg/dream1.png"
image bg umbrella ="bg/under_umbrella.png"
image bg test_room ="bg/test_room.png"
image bg rain ="bg/rain.png"
image bg theatre ="bg/theatre.png"
image bg shop ="bg/shop.png"
image bg awak ="bg/awak.png"
#结局
image bg end_1 ="end/end_1_1.png"
image bg end_2 ="end/end_2_1.png"
image bg end_3 ="end/end_3_3.png"
#道具
image tool crystal_ball = 'tool/crystal_ball.png'
image tool present = 'tool/present.png'
image tool notebook = 'tool/notebook.png'
image tool dog_toy = 'tool/dog_toy.png'
# 定义水晶球普通状态和发光状态
image crystal_ball_glow:
    "images/tool/crystal_ball glow.png"  # 发光版图片（带光晕/高光）
    alpha 0.0
    linear 0.5 alpha 1.0            # 0.5秒渐亮
    pause 0.3                       # 高亮停留
    linear 0.3 alpha 0.0            # 渐暗（可选，若直接跳转会省略此步）

# 定义一个全屏白光闪烁作为辅助反馈（复用你之前的flash）
define flash = Fade(0.1, 0.0, 0.1, color="#fff")
#音效
define rain = 'snd/rain.wav'
#bgm
define theatre = 'bgm/theatre1.mp3'
define test = 'bgm/test.mp3'
define sad = 'bgm/sad.mp3'
define life = 'bgm/life.mp3'
define shop1 = 'bgm/shop1.mp3'
define shop2 = 'bgm/shop2.mp3'
define room = 'bgm/room.mp3'
define dream = 'bgm/dream.mp3'
define wind = 'bgm/wind.mp3'
define bad = 'bgm/bad.mp3'
define demon = 'bgm/demon.mp3'
# 游戏在此开始。

label start:
    jump end_three
    scene bg dream with dissolve:
        vp
    '''有人说，我们之间隔着一整个青春的距离。
    可每当风吹过旧教室的窗棂，我总能听见你的名字，像一句未说完的话，卡在时光的缝隙里。
    那些并肩走过的黄昏、欲言又止的对视、藏在日记本里不敢署名的句子……它们究竟是爱情，还是比爱情更沉默的陪伴？'''
    '''我不知道答案。
    我只知道，有些故事从未真正结束——它们只是换了一种方式，在我们各自走向未来的路上，悄悄亮着。
    而今天，我想把这段光，重新讲给你听。'''
    "这是关于两个女孩之间的故事，也许是爱情，也许是友情，也许只有过去可以回忆，也许还有未来可以追寻"


    call screen crystal_choice


