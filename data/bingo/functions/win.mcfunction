title @a title {"text":"Bingo!", "bold":true}
title @a subtitle {"text":"", "bold":true, "extra":[{"selector":"@s"},{"text":" has won the game!"}]}
advancement grant @s only bingo:win
execute at @a run playsound minecraft:ui.toast.challenge_complete player @a