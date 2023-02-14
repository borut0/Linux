import os
import subprocess

from libqtile import bar, layout, widget, qtile
from libqtile.config import Click, Drag, ScratchPad, DropDown, Group, Key, Match, Screen
from libqtile.lazy import lazy

from libqtile import hook
from libqtile import extension

from theme import catppuccin

mod = "mod4"
terminal = "alacritty"
browser = "google-chrome-stable"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod, "shift"],"Return", lazy.layout.toggle_split(),desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "x", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle Fullscreen"),
    Key([mod, "shift"], "space", lazy.window.toggle_floating(), desc="Toggle Floating"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # dmenu
    Key([mod], "p", lazy.spawn("dmenu_run -p '  '"), desc="For Searching"),
    # browser
    Key([mod], "b", lazy.spawn(browser), desc="For Browsing"),
    # clipBoard
    # Key([mod], "v", lazy.spawn("copyq menu"), desc="CilpBoard"),
]

groups = [
    Group(
        "1",
        label="",
        layout="Columns",
    ),
    Group(
        "2",
        label="",
        layout="MonadTall",
    ),
    Group(
        "3",
        label="",
        layout="MonadTall",
    ),
    Group(
        "4",
        label="",
        layout="MonadTall",
        matches = [Match(wm_class = 'qutebrowser')]
    ),
    Group(
        "5",
        label="",
        layout="=MonadTall",
    ),
    Group(
        "6",
        label="",
        layout="MonadTall",
    ),
    Group(
        "7",
        label="",
        layout="Tile",
    ),
    Group(
        "8",
        label="",
        layout="max",
        matches = []
    ),
    Group(
        "9",
        label="",
        layout="Columns",
        matches=[Match(wm_class = 'google-chrome-stable')]
    ),
]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name),
            ),
        ]
    )

layouts = [
    layout.Tile(
        border_focus=catppuccin["Green"],
        border_normal=catppuccin["Crust"],
        border_width=3,
        margin=8,
    ),
    layout.Columns(
        border_focus=catppuccin["Green"],
        border_normal=catppuccin["Crust"],
        border_width=3,
        margin=8,
    ),
    layout.Max(
        margin=30,
        border_focus=catppuccin["Green"],
        border_normal=catppuccin["Crust"],
        border_width=0,
    ),
    # Layouts:
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(
        margin=8,
        border_focus=catppuccin["Green"],
        border_normal=catppuccin["Crust"],
        border_width=3,
    ),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.Floating(
        border_width = 0
    )
]

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    text="",
                    padding=10,
                    fontsize=20,
                    foreground=catppuccin["Green"],
                    background=catppuccin["Crust"],
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn('code')},
                ),
                widget.TextBox(
                    text = "〉",
                    padding=0,
                    fontsize=20,
                    background=catppuccin["Crust"],
                    foreground=catppuccin["Green"],
                ),
                widget.GroupBox(
                    highlight_method="text",
                    this_current_screen_border=catppuccin["Green"],
                    urgent_alert_method="text",
                    urgent_text=catppuccin["Yellow"],
                    background=catppuccin["Base"],
                    active=catppuccin["Text"],
                    inactive=catppuccin["Surface0"],
                    fontsize=15,
                    disable_drag=True,
                ),
                widget.TextBox(
                    text = "〉",
                    padding=0,
                    fontsize=20,
                    background=catppuccin["Base"],
                    foreground=catppuccin["Green"],
                ),
                widget.WindowName(
                    background=catppuccin["Base"],
                    padding = 10
                ),
                widget.TextBox(
                    text="〈",
                    padding=2,
                    fontsize=22,
                    background=catppuccin["Base"],
                    foreground=catppuccin["Green"],
                ),
                 widget.TextBox(
                    text='',
                    background=catppuccin["Base"],
                    foreground=catppuccin["Text"],
                    padding=2
                ),
                widget.Battery(
                    charge_char='*', discharge_char='', full_char='',
                    format= "{char} {percent:2.0%} "
                ),
                widget.TextBox(
                    text="〈",
                    fontsize=22,
                    background=catppuccin["Base"],
                    foreground=catppuccin["Green"],
                ),
                 widget.TextBox(
                    text='',
                    background=catppuccin["Base"],
                    foreground=catppuccin["Text"],
                    padding=2,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("pavucontrol")},
                ),
                widget.PulseVolume(
                    padding = 10 
                ),
                widget.TextBox(
                    text="〈",
                    fontsize=22,
                    background=catppuccin["Base"],
                    foreground=catppuccin["Green"],
                ),
                widget.Memory(
                    foreground=catppuccin["Text"],
                    format='RAM {MemPercent: .0f}%',
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                ),
                widget.TextBox(
                    text="〈",
                    padding=4,
                    fontsize=22,
                    background=catppuccin["Base"],
                    foreground=catppuccin["Green"],
                ),
                widget.CPU(
                    background=catppuccin["Base"],
                    foreground=catppuccin["Text"],
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                    format=" {load_percent}%",
                    padding=5,
                ),
                widget.TextBox(
                    text="〈",
                    padding=4,
                    fontsize=22,
                    background=catppuccin["Base"],
                    foreground=catppuccin["Green"],
                ),
                widget.TextBox(
                    text=' ',
                    background=catppuccin["Base"],
                    foreground=catppuccin["Text"],
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(terminal + ' -e sudo pacman -Syu')},
                    padding=2
                ),
                widget.CheckUpdates(
                    update_interval=18000,
                    display_format="{updates}",
                    no_update_string='0',
                    colour_have_updates=catppuccin["Crust"],
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(terminal + ' -e sudo pacman -Syu')},
                    background=catppuccin["Base"]
                ),
                widget.TextBox(
                    text="〈",
                    padding=2,
                    fontsize=22,
                    background=catppuccin["Base"],
                    foreground=catppuccin["Green"],
                ),
                widget.Net(
                    interface="wlp3s0",
                    format="{down} ↓↑{up}",
                    background=catppuccin["Base"],
                    foreground=catppuccin["Text"],
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(terminal + ' -e nmcli d wifi list')},
                    update_interval=1.0,
                ),
                widget.TextBox(
                    text="〈",
                    padding=2,
                    fontsize=22,
                    background=catppuccin["Base"],
                    foreground=catppuccin["Green"],
                ),
                widget.Net(
                    interface="enp0s20f0u2",
                    format="{down} ↓↑{up}",
                    background=catppuccin["Base"],
                    foreground=catppuccin["Text"],
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(terminal + ' -e nmcli d wifi list')},
                    update_interval=1.0,
                ),
                widget.NvidiaSensors(
                    format='GPU {temp}°C',
                    background=catppuccin["Base"],
                    foreground=catppuccin["Text"],
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn('nvidia-settings')},
                ),
                widget.TextBox(
                    text="〈",
                    padding=4,
                    fontsize=22,
                    background=catppuccin["Base"],
                    foreground=catppuccin["Green"],
                ),
                 widget.TextBox(
                    text='',
                    background=catppuccin["Base"],
                    foreground=catppuccin["Text"],
                    padding=2
                ),
                widget.Clock(
                    format="%I:%M %p",
                    background=catppuccin["Base"],
                    foreground=catppuccin["Text"],
                ),
                widget.TextBox(
                    text="〈",
                    padding=4,
                    fontsize=22,
                    background=catppuccin["Base"],
                    foreground=catppuccin["Green"],
                ),
                widget.Systray(
                    background=catppuccin["Base"],
                ),
                widget.TextBox(
                    text="〈",
                    padding=4,
                    fontsize=22,
                    background=catppuccin["Base"],
                    foreground=catppuccin["Green"],
                ),
                
                widget.Clock(
                    format="%a %d-%m-%Y",
                    background=catppuccin["Base"],
                    foreground=catppuccin["Text"],
                ),
                widget.TextBox(
                    text="",
                    # text="〈",
                    padding=0,
                    fontsize=22,
                    background=catppuccin["Base"],
                    foreground=catppuccin["Green"],
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/Icons")],
                    scale=0.7,
                    background=catppuccin["Green"],
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=22,
                    background=catppuccin["Green"],
                    foreground=catppuccin["Base"],
                ),
                widget.TextBox(
                    text=" ",
                    background=catppuccin["Base"],
                    foreground=catppuccin["Green"],
                    fontsize=15,
                    mouse_callbacks={
                        "Button1": lazy.shutdown(),
                    },
                ),
            ],
            24,
            background=catppuccin["Base"],
            foreground=catppuccin["Text"],
            margin = [10,10,2,10],
            opacity = .9,
        ),
    ),
]

mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False 
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # xprop
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="flameshot"),
    ],
    border_width=2,
    border_focus=catppuccin["Lavender"],
    border_normal=catppuccin["Crust"],
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits;
wmname = "LG3D"

