<!DOCTYPE html>
<html>
<head>
  <title>Mini Arcade 🎮</title>
  <style>
    body { font-family: Arial; text-align: center; background: #111; color: white; }
    .menu button { margin: 10px; padding: 10px 20px; font-size: 16px; }
    .game { display: none; margin-top: 20px; }
    .grid { display: grid; grid-template-columns: repeat(3, 80px); gap: 5px; justify-content: center; }
    .cell { width: 80px; height: 80px; background: #333; font-size: 30px; display:flex; align-items:center; justify-content:center; cursor:pointer; }
    .box { width: 200px; height: 200px; margin: auto; background: red; }
  </style>
</head>
<body>

<h1>🎮 Mini Arcade</h1>

<div class="menu">
  <button onclick="showGame('guess')">Guess Number</button>
  <button onclick="showGame('tic')">Tic Tac Toe</button>
  <button onclick="showGame('react')">Reaction Test</button>
</div>

<!-- Guess Game -->
<div id="guess" class="game">
  <h2>Guess the Number</h2>
  <input id="guessInput" type="number">
  <button onclick="checkGuess()">Guess</button>
  <p id="guessResult"></p>
</div>

<!-- Tic Tac Toe -->
<div id="tic" class="game">
  <h2>Tic Tac Toe</h2>
  <div class="grid" id="grid"></div>
  <p id="ticResult"></p>
</div>

<!-- Reaction Game -->
<div id="react" class="game">
  <h2>Reaction Test</h2>
  <div class="box" id="box" onclick="clickBox()"></div>
  <p id="reactResult"></p>
</div>

<script>
function showGame(id){
  document.querySelectorAll('.game').forEach(g=>g.style.display='none');
  document.getElementById(id).style.display='block';
}

/* Guess Game */
let num = Math.floor(Math.random()*100)+1;
function checkGuess(){
  let val = document.getElementById("guessInput").value;
  if(val == num) document.getElementById("guessResult").innerText="Correct!";
  else if(val > num) document.getElementById("guessResult").innerText="Too High";
  else document.getElementById("guessResult").innerText="Too Low";
}

/* Tic Tac Toe */
let current = "X";
let board = ["","","","","","","","",""];
let grid = document.getElementById("grid");

board.forEach((_,i)=>{
  let cell = document.createElement("div");
  cell.className="cell";
  cell.onclick=()=>move(i,cell);
  grid.appendChild(cell);
});

function move(i,cell){
  if(board[i]!="") return;
  board[i]=current;
  cell.innerText=current;
  if(checkWin()) document.getElementById("ticResult").innerText=current+" Wins!";
  current = current=="X"?"O":"X";
}

function checkWin(){
  let wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
  return wins.some(w=> w.every(i=>board[i]==current));
}

/* Reaction Game */
let startTime;
setTimeout(()=>{
  document.getElementById("box").style.background="green";
  startTime = new Date().getTime();
}, Math.random()*3000+2000);

function clickBox(){
  let time = new Date().getTime() - startTime;
  document.getElementById("reactResult").innerText="Time: "+time+" ms";
}
</script>

</body>
</html>
