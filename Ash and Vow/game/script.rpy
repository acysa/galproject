"""全套素材文案（适配 AI 绘图 / AI 音乐生成，按文件夹分类，直接复制使用）
整体世界观风格：中世纪欧式暗黑奇幻、边境逃亡、旧神遗迹、黯蚀骑士题材，整体色调偏暗沉、冷色调，氛围压抑、悬疑，穿插战斗、静谧、旅途等不同情绪。

10. wildroad_cross.png
描述：野外荒野岔路口，两条土路向不同方向延伸，地面长满荒草，林间雾气弥漫，天色昏暗，前路未知，荒凉苍茫的野外道路。
11. forest_road.png
描述：拂晓时分的林间主干道，道路笔直延伸向密林深处，两侧古树林立，天边泛着微光，雾气淡淡消散，氛围庄重悠远，适合结伴远行场景。"""




# ====================== 全局变量 & 基础配置 ======================
default player_name = _("凯伦")  # 主角默认名字
default trust_father = 0        # 神父好感度
default trust_isol = 0           # 伊索尔德好感度
default player_mark = True     # 男主拥有血脉印记（核心伏笔）
default combat_power = 25    #主角战斗力

# 角色定义
define karen = Character("[player_name]", color="#4a86e8")
define marcus = Character(_("马库斯神父"), color="#8b7355")
define isold = Character(_("伊索尔德"), color="#39ac73")
define old_man = Character("老人")
define black_knight_cap = Character("黑骑士")
define narrator = Character(None)

# ====================== 图片资源声明（自行替换素材）======================
# 场景图
image bg church_rain = "bg/church_rain.png"       # 雨夜破教堂
image bg church_inner = "bg/church_inner.png"    # 教堂内室暖景
image bg church_tower = "bg/church_tower.png"    # 深夜钟楼
image bg town_gate_dark = "bg/town_gate_dark.png"# 镇口黑骑士剪影
# 第一章新增场景
image bg forest_tunnel = "bg/forest_tunnel.png"    # 林间密道
image bg hunter_hut = "bg/hunter_hut.png"          # 猎人小屋
image bg town_street = "bg/town_street.png"        # 小镇街巷
image bg forest_road = "bg/forest_road.png"        # 林间大路
image bg altar_cave = "bg/altar_cave.png" # 地下黑雾祭坛洞窟
image bg altar_core = "bg/altar_core.png" # 祭坛黑暗核心中枢
image bg secret_tunnel = "bg/secret_tunnel.png" # 隐秘潜行暗道
image bg hermit_hut = "bg/hermit_hut.png" # 林间隐士居所
image bg altar_boss_arena = "bg/altar_boss_arena.png" # 骑士统领决战场地
image bg forest_road2 = "bg/forest_road2.png" # 林间通路（承接第二章）

# 立绘
image char karen_normal = "char/karen_normal.png"
image char marcus_normal = "char/marcus_normal.png"
image char isold_normal = "char/isold_normal.png"
image char old_man = "char/old_man.png" # 囚禁长老NPC
image char black_knight_cap = "char/black_knight_cap.png" # 黑刃骑士队长NPC
# 特效图
image effect mark_glow = "effect/mark_glow.png"  # 手腕印记发光特效
# 特效
#image effect mark_glow = "CG/mark_glow.mp4"
image effect ember_combine = "CG/ember_combine.mp4" # 双人烬火合击特效
image effect dark_mist_erode = "CG/dark_mist_erode.mp4" # 黯蚀黑雾腐蚀特效
image effect tear_glow = "CG/tear_glow.mp4"# 落泪高光CG特效
image start movie = Movie(play="audio/CG/1.mp4") 

# ====================== 图片资源 ======================
# 通用场景
image bg town_gate_dark = "bg/town_gate_dark.png"
image bg tunnel_dark = "bg/tunnel_dark.png"
image bg rain_forest = "bg/rain_forest.png"
image bg forest_clearing = "bg/forest_clearing.png"
image bg hunter_hut = "bg/hunter_hut.png"
image bg church_hall_dawn = "bg/church_hall_dawn.png"
image bg town_street_day = "bg/town_street_day.png"
image bg church_courtyard = "bg/church_courtyard.png"
image bg town_outside_night = "bg/town_outside_night.png"
image bg wildroad_cross = "bg/wildroad_cross.png"
image bg forest_road = "bg/forest_road.png"
image bg mist_forest = "bg/mist_forest.png"
image bg ancient_ruins = "bg/ancient_ruins.png"
image bg forest_hideout = "bg/forest_hideout.png"
image bg town_outskirt = "bg/town_outskirt.png"
image bg blood_altar_mountain = "bg/blood_altar_mountain.png" # 后山血脉黑石祭坛
image bg dead_forest_path = "bg/dead_forest_path.png" # 荒芜枯林密道
image bg abandon_castle_ruin = "bg/abandon_castle_ruin.png" # 废弃古堡废墟
image bg fog_forest_battle = "bg/fog_forest_battle.png" # 骑士围剿林地战场


#结局
image bg end_1 = "bg/end_1.png" # 血染祭坛
image bg end_2 = "bg/end_2.png" #献祭轮回
image bg end_3 = "bg/end_3.png"#迷雾囚禁
image bg end_4 = "bg/end_4.png"#祭坛囚笼

# ====================== 音效 & BGM ======================

define sound.crash = "snd/crash.wav"
define sound.crow = "snd/crow.wav"
define sound.fight = "snd/fight.wav"
define sound.whisper = "snd/whisper.wav"
define sound.retreat = "snd/retreat.wav"
define sound.crowd_murmur = "snd/crowd_murmur.wav"
define sound.horse = "snd/horse.wav"
define sound.signal_fire = "snd/signal_fire.wav"
define sound.knight_rush = "snd/knight_rush.wav"
define sound.magic_barrier = "snd/magic_barrier.wav"
define sound.footstep = "snd/footstep.wav" # 新增：符文屏障音效
define sound.whisper_ghost = "snd/whisper_ghost.wav"
define sound.monster_roar = "snd/monster_roar.wav"
define sound.camp_noise = "snd/camp_noise.wav"
define sound.chain_drag = "snd/chain_drag.wav" # 锁链拖拽声
define sound.altar_hum = "snd/altar_hum.wav" # 法阵低频嗡鸣
define sound.stealth_step = "snd/stealth_step.wav" # 潜行轻脚步声
define sound.boss_clash = "snd/boss_clash.wav" # BOSS重兵器碰撞声
define sound.soft_campfire = "snd/soft_campfire.wav" # 篝火环境音
define sound.march_armor = "snd/march_armor.wav" # 骑士行军重甲声
define sound.footstep1 = "snd/footstep1.wav" # 林间步行脚步声

define bgm_danger = "bgm/bgm_danger.mp3"
define bgm_tunnel = "bgm/bgm_tunnel.mp3"
define bgm_forest = "bgm/bgm_forest.mp3"
define bgm_hut_safe = "bgm/bgm_hut_safe.mp3"
define bgm_dawn_quiet = "bgm/bgm_dawn_quiet.mp3"
define bgm_town_suspense = "bgm/bgm_town_suspense.mp3"
define bgm_night_tension = "bgm/bgm_night_tension.mp3"
define bgm_solemn = "bgm/bgm_solemn.mp3" # 新增：凝重叙事BGM
define bgm_rain = "bgm/bgm_rain.mp3"      # 雨夜压抑BGM
define bgm_warm = "bgm/bgm_warm.mp3"      # 室内温馨BGM
define bgm_mist_tension = "bgm/bgm_mist_tension.mp3"
define bgm_hide_quiet = "bgm/bgm_hide_quiet.mp3"
define bgm_town_wary = "bgm/bgm_town_wary.mp3"
define bgm_altar_tension = "bgm/bgm_altar_tension.mp3" # 洞窟压抑主旋律
define bgm_stealth_quiet = "bgm/bgm_stealth_quiet.mp3" # 潜行静谧曲
define bgm_boss_fight = "bgm/bgm_bgm_boss_fight.mp3" # 决战激昂战斗曲
define bgm_hermit_warm = "bgm/bgm_hermit_warm.mp3" # 隐士居所温情BGM
define bgm_sad_break = "bgm/bgm_sad_break.mp3" # 决裂悲伤BGM
define bgm_solemn2 = "bgm/bgm_solemn2.mp3" # 林间行路叙事曲



#你个傻逼

# ====================== 游戏入口：自定义名字 ======================
label start:
    # 游戏内改名窗口
    $ player_name = renpy.input("请为你的角色命名：", length=10)
    # 清空空格/空内容时，恢复默认名
    $ player_name = player_name.strip()
    if not player_name:
        $ player_name = _("凯伦")

    jump prologue



