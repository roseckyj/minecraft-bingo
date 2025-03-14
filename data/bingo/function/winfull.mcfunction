title @a title {"text":"Bingo master!", "bold":true, "color":"gold"}
title @a subtitle {"text":"", "bold":true, "color":"gold", "extra":[{"selector":"@s"},{"text":" completed the whole card!"}]}
execute at @a run playsound minecraft:ui.toast.challenge_complete player @a

advancement grant @s only bingo:win/win
advancement grant @s only bingo:win/winfull
advancement grant @s only bingo:win/winnow

gamemode creative @s