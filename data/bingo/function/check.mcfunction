advancement grant @s only bingo:win/getone
function bingo:shareadvancement

execute if entity @s[advancements={bingo:win/winfull=false,bingo:generated/a11=true,bingo:generated/a21=true,bingo:generated/a31=true,bingo:generated/a41=true,bingo:generated/a51=true,bingo:generated/b12=true,bingo:generated/b22=true,bingo:generated/b32=true,bingo:generated/b42=true,bingo:generated/b52=true,bingo:generated/c13=true,bingo:generated/c23=true,bingo:generated/c33=true,bingo:generated/c43=true,bingo:generated/c53=true,bingo:generated/d14=true,bingo:generated/d24=true,bingo:generated/d34=true,bingo:generated/d44=true,bingo:generated/d54=true,bingo:generated/e15=true,bingo:generated/e25=true,bingo:generated/e35=true,bingo:generated/e45=true,bingo:generated/e55=true}] run function bingo:winfull

execute if entity @s[advancements={bingo:win/winfull=false,bingo:win/winnow=false,bingo:win/winx1=false,bingo:generated/a11=true,bingo:generated/a21=true,bingo:generated/a31=true,bingo:generated/a41=true,bingo:generated/a51=true}] run function bingo:winx1
execute if entity @s[advancements={bingo:win/winfull=false,bingo:win/winnow=false,bingo:win/winx2=false,bingo:generated/b12=true,bingo:generated/b22=true,bingo:generated/b32=true,bingo:generated/b42=true,bingo:generated/b52=true}] run function bingo:winx2
execute if entity @s[advancements={bingo:win/winfull=false,bingo:win/winnow=false,bingo:win/winx3=false,bingo:generated/c13=true,bingo:generated/c23=true,bingo:generated/c33=true,bingo:generated/c43=true,bingo:generated/c53=true}] run function bingo:winx3
execute if entity @s[advancements={bingo:win/winfull=false,bingo:win/winnow=false,bingo:win/winx4=false,bingo:generated/d14=true,bingo:generated/d24=true,bingo:generated/d34=true,bingo:generated/d44=true,bingo:generated/d54=true}] run function bingo:winx4
execute if entity @s[advancements={bingo:win/winfull=false,bingo:win/winnow=false,bingo:win/winx5=false,bingo:generated/e15=true,bingo:generated/e25=true,bingo:generated/e35=true,bingo:generated/e45=true,bingo:generated/e55=true}] run function bingo:winx5

execute if entity @s[advancements={bingo:win/winfull=false,bingo:win/winnow=false,bingo:win/win1x=false,bingo:generated/a11=true,bingo:generated/b12=true,bingo:generated/c13=true,bingo:generated/d14=true,bingo:generated/e15=true}] run function bingo:win1x
execute if entity @s[advancements={bingo:win/winfull=false,bingo:win/winnow=false,bingo:win/win2x=false,bingo:generated/a21=true,bingo:generated/b22=true,bingo:generated/c23=true,bingo:generated/d24=true,bingo:generated/e25=true}] run function bingo:win2x
execute if entity @s[advancements={bingo:win/winfull=false,bingo:win/winnow=false,bingo:win/win3x=false,bingo:generated/a31=true,bingo:generated/b32=true,bingo:generated/c33=true,bingo:generated/d34=true,bingo:generated/e35=true}] run function bingo:win3x
execute if entity @s[advancements={bingo:win/winfull=false,bingo:win/winnow=false,bingo:win/win4x=false,bingo:generated/a41=true,bingo:generated/b42=true,bingo:generated/c43=true,bingo:generated/d44=true,bingo:generated/e45=true}] run function bingo:win4x
execute if entity @s[advancements={bingo:win/winfull=false,bingo:win/winnow=false,bingo:win/win5x=false,bingo:generated/a51=true,bingo:generated/b52=true,bingo:generated/c53=true,bingo:generated/d54=true,bingo:generated/e55=true}] run function bingo:win5x

advancement revoke @a only bingo:win/winnow