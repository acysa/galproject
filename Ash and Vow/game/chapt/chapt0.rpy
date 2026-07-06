
# ====================== 序章主剧情 ======================
label prologue:
    scene bg church_rain:
        xsize 1920
        ysize 1080
        xalign 0.5
        yalign 0.5
    play music bgm_rain fadeout 1.0 fadein 2.0
    play sound rain loop

    narrator "旧神的荣光早已沉入灰海，魔法成了禁忌的传说，骑士的铠甲锈在历史里。"
    narrator "凡人在破碎的大陆上苟活，守着仅存的灯火，假装看不见黑暗里窥伺的眼。"
    $ renpy.movie_cutscene("1.mp4")

    show karen_normal at left:
        yoffset -280
        zoom(0.3)
        xzoom(-1.0)
    karen "(缩在石柱旁，外衣被雨水浸透，冰冷的寒意顺着四肢蔓延)"
    karen "再走下去……腿就要撑不住了。"

    play music sound.footstep
    show marcus_normal at right:
        yoffset 0
        zoom(0.4)
        xzoom(-1.0)
    marcus "孩子，外面的雨会吞掉活人。进来吧。这里不收留罪孽，只收留活下来的人。"

    karen "(抬头，眼神满是逃亡者的警惕)"
    karen "我……不麻烦您。我歇一会儿就离开。"

    marcus "(蹲下身，烛火映亮你脸上的泥污与疲惫)"
    marcus "从南边猩红隘口逃来的，对吗？那些黑甲人，已经烧毁了七个村落。"

    # 第一分支：坦诚 / 戒备
    menu:
        "【坦诚】您怎么看出来的？村子……已经没了。":
            jump branch_truth
        "【戒备】我只是路过，和那边没关系。":
            jump branch_wary

# ---------------------- 分支1：坦诚路线 ----------------------
label branch_truth:
    $ trust_father += 1
    karen "(声音压抑沙哑)"
    karen "他们见人就杀……我是唯一跑出来的。"

    marcus "(轻轻叹气，目光骤然落在你的左手腕上)"
    marcus "……！"

    play movie "CG/wrist.mp4"
# 印记闪光特效
    pause 1.0
#    hide effect mark_glow

    marcus "(压低声音，神色凝重)"
    marcus "你手腕上的印记——它刚才亮了。"

    karen "(慌忙抬手捂住手腕，面露惊愕)"
    karen "那不是胎记……？从我记事起，它就一直存在。"

    marcus "这绝非胎记，是「旧神余烬」的印记。"
    marcus "他们追杀你，并非因为你是难民，而是觊觎你身上潜藏的力量。"

    jump scene_church_inner

# ---------------------- 分支2：戒备路线 ----------------------
label branch_wary:
    karen "(偏过头，语气生硬疏离)"
    karen "我没有过去。"

    marcus "(沉默片刻，不再追问，递来一块干燥麻布)"
    marcus "过去可以丢掉，但性命不能。"
    marcus "(转身添柴，低声自语)"
    marcus "……还是来了，和预言里一样。"

    jump scene_church_inner

# ---------------------- 过渡：教堂内室 中段剧情 ----------------------
label scene_church_inner:
    scene bg church_inner:
        xsize 1920
        ysize 1080
        xalign 0.5
        yalign 0.5
    play bgm bgm_warm fadeout 1.0 fadein 2.0
    stop rain
    show char marcus_normal at right:
        zoom(0.4)
        xzoom(-1.0)

    marcus "霜鸦镇地处边境夹缝，王室鞭长莫及，黑甲骑士也极少踏足此地。"
    marcus "你可以暂时留在这里，帮我打理教堂，换一口热饭与安身之处。"
    show char karen_normal at left:
        yoffset -280
        zoom(0.3)
        xzoom(-1.0)

    karen "(心中微动，长久逃亡后难得感到一丝安稳)"
    karen "终于……能停下来喘口气了吗？"

    play sound door
    show isold_normal warm at right:
        zoom(0.4)
    isold "神父，我送消炎草和安眠草来了……这位是？"

    marcus "新来的少年，名叫[player_name]，从南边逃难而来。"

    isold "(看向你，眼神锐利却带着善意，轻轻点头)"
    isold "夜里千万不要靠近森林。最近鸦群聚集，绝非寻常景象。"
    isold "镇上有人目击，黑甲骑兵一直在林外徘徊。"

    karen "(心头一沉，想起一路的追杀)"
    karen "……我明白了，多谢提醒。"

    jump scene_tower_night

# ---------------------- 高潮：深夜钟楼 危机降临 ----------------------
label scene_tower_night:
    scene bg church_tower:
        xsize 1920
        ysize 1080
        xalign 0.5
        yalign 0.5
    play bgm bgm_danger fadeout 1.0 fadein 2.0

    hide char marcus_normal
    hide char isold_normal
    show char karen_normal at left:
        zoom(0.2)
        xzoom(-1.0)
        yoffset -280

    karen "(深夜辗转难眠，独自走上钟楼，推开木窗望向夜色)"
    karen "(内心思索)我到底是谁？那个神秘的印记，又究竟代表着什么？"

    play music sound.horse loop
    play music sound.crow loop
    scene bg town_gate_dark with fade:
        xsize 1920
        ysize 1080
        xalign 0.5
        yalign 0.5
    narrator "远处的道路上，一道道漆黑的骑士剪影缓缓出现，冰冷的压迫感席卷整座小镇。"

    karen "(身体瞬间僵住，呼吸一滞)"
    karen "他们……终究还是追过来了！"

    show char marcus_normal at left:
        zoom(0.4)
    marcus "(快步上前按住你的手臂，神情严肃)"
    marcus "听着，[player_name]！他们的目标自始至终都是你！"
    marcus "(将一枚古朴铜徽塞进你手中)"
    marcus "去找伊索尔德，她知晓地窖的密道！记住——你从来都不只是一个逃亡者，你是残存的火种。"

    show char isold_normal at right:
        zoom(2.0)
        yoffset -158
    isold "(手握短刀，神色果决)"
    isold "跟我走！密道直通后山森林，现在立刻动身！"

    karen "(紧紧攥住铜徽，手腕处的印记微微发烫)"
    karen "我……不想再一味逃跑了。"

    # 序章最终二选一选项

    menu:
        "我跟你们走！":
            jump judge_route   # 进入主线分流判断
        "我留下来挡一阵，你们先撤！":
            $combat_power+=6
            jump route_3       # 直接进入路线3 力量觉醒线

# ====================== 核心分流入口：根据 trust_father 判断进入路线1 / 路线2 ======================
label judge_route:
    stop horse
    stop crow

    if trust_father == 1:
        jump route_1   # 神父高信任 → 路线1 林间追踪
    else:
        jump route_2   # 神父低信任 → 路线2 小镇阴谋
