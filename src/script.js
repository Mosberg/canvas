// Load JSON data
const playerData = JSON.parse(localStorage.getItem("data/playerData"));
const gameData = JSON.parse(localStorage.getItem("data/gameData"));

// Set player avatar and name
document.getElementById("player-avatar").src = playerData.player.src;
document.getElementById("player-name").textContent = playerData.player.name;

// Set skill icon, level, and experience
document.getElementById("skill-icon").src = gameData.src;
document.getElementById("skill-level-value").textContent =
  playerData.player.skills.level;
document.getElementById("skill-experience-value").textContent =
  playerData.player.skills.experience;

// Generate axe list
const axeList = document.getElementById("axe-list");
gameData.items.axes.forEach((axe) => {
  const axeListItem = document.createElement("li");
  axeListItem.innerHTML = `<img src="${axe.src}" alt="${axe.alt}"> ${axe.title}`;
  axeList.appendChild(axeListItem);
});

// Generate tree list
const treeList = document.getElementById("tree-list");
gameData.objects.trees.forEach((tree) => {
  const treeListItem = document.createElement("li");
  treeListItem.innerHTML = `<img src="${tree.src}" alt="${tree.alt}"> ${tree.title}`;
  treeList.appendChild(treeListItem);
});

// Generate log list
const logList = document.getElementById("log-list");
gameData.resources.logs.forEach((log) => {
  const logListItem = document.createElement("li");
  logListItem.innerHTML = `<img src="${log.src}" alt="${log.alt}"> ${log.title}`;
  logList.appendChild(logListItem);
});
