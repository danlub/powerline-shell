from powerline_shell.themes.default import DefaultColor


class Color(DefaultColor):
    """Basic theme which only uses colors in 0-15 range"""
    
    # Web con los colores!
    # https://misc.flogisoft.com/bash/tip_colors_and_formatting
    
    RESET = -1
    
    USERNAME_FG = 39
    USERNAME_BG = 230
    USERNAME_ROOT_BG = 124

    HOSTNAME_FG = 230
    HOSTNAME_BG = 39 # 238

    HOME_SPECIAL_DISPLAY = True
    HOME_BG = 31  # blueish
    HOME_FG = 15  # white
    PATH_BG = 237  # dark grey
    PATH_FG = 250  # light grey
    CWD_FG = 254  # nearly-white grey
    SEPARATOR_FG = 244

    READONLY_BG = 1
    READONLY_FG = 15

    REPO_CLEAN_BG = 148  # a light green color
    REPO_CLEAN_FG = 0  # black
    REPO_DIRTY_BG = 161  # pink/red
    REPO_DIRTY_FG = 15  # white

    CMD_PASSED_BG = 236
    CMD_PASSED_FG = 15
    CMD_FAILED_BG = 161
    CMD_FAILED_FG = 15

    JOBS_FG = 39
    JOBS_BG = 238

    GIT_STASH_BG = 221
    GIT_STASH_FG = 0

    TIME_FG = 230
    TIME_BG = 238
