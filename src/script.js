// Load player data
fetch("/src/data/playerData.json")
  .then((response) => response.json())
  .then((data) => {
    const playerData = data;
    const playerAvatarElement = document.getElementById("player-avatar");
    const playerNameElement = document.getElementById("player-name");
    playerAvatarElement.src = playerData.player.src;
    playerNameElement.textContent = playerData.player.name;

    // Load game data
    fetch("/src/data/woodcuttingData.json")
      .then((response) => response.json())
      .then((data) => {
        const gameData = data;
        const skillIconElement = document.getElementById("skill-icon");
        const skillLevelElement = document.getElementById("skill-level-value");
        const skillExperienceElement = document.getElementById(
          "skill-experience-value"
        );
        skillIconElement.src = gameData.src;
        skillLevelElement.textContent = playerData.player.skills.level;
        skillExperienceElement.textContent =
          playerData.player.skills.experience;

        // Generate axe list
        const axeListElement = document.getElementById("axe-list");
        gameData.items.axes.forEach((axe) => {
          const axeListItem = document.createElement("li");
          axeListItem.innerHTML = `<img src="${axe.src}" alt="${axe.alt}"> ${axe.title}`;
          axeListElement.appendChild(axeListItem);
        });

        // Generate tree list
        const treeListElement = document.getElementById("tree-list");
        gameData.objects.trees.forEach((tree) => {
          const treeListItem = document.createElement("li");
          treeListItem.innerHTML = `<img src="${tree.src}" alt="${tree.alt}"> ${tree.title}`;
          treeListElement.appendChild(treeListItem);
        });

        // Generate log list
        const logListElement = document.getElementById("log-list");
        gameData.resources.logs.forEach((log) => {
          const logListItem = document.createElement("li");
          logListItem.innerHTML = `<img src="${log.src}" alt="${log.alt}"> ${log.title}`;
          logListElement.appendChild(logListItem);
        });
      });
  });
