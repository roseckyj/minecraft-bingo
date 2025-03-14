execute if entity @s[advancements={bingo:win/win=false}] run title @a title {"text":"Bingo!", "bold":true}
execute if entity @s[advancements={bingo:win/win=false}] run title @a subtitle {"text":"", "bold":true, "extra":[{"selector":"@s"},{"text":" got a bingo!"}]}
execute if entity @s[advancements={bingo:win/win=false}] at @a run playsound minecraft:ui.toast.challenge_complete player @a

execute if entity @s[advancements={bingo:win/win=true}] run title @a title {"text":"", "bold":true}
execute if entity @s[advancements={bingo:win/win=true}] run title @a subtitle {"text":"", "bold":true, "extra":[{"selector":"@s"},{"text":" got another bingo!"}]}
execute if entity @s[advancements={bingo:win/win=true}] run advancement grant @s only bingo:win/wintwo

advancement grant @s only bingo:win/win
advancement grant @s only bingo:win/win3x
advancement grant @s only bingo:win/winnow