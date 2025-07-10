function getLinksAll() {
    fetch("/api/allLinks").then((response) => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error("Uhoh cant get links");
        }
    })
        .then((data) => {
            if (data.length > 0) {
                showLinks(data);
            } else {
                let list = document.getElementById("listOfLinks")
                let li = document.createElement("li");
                li.className = "bg-stone-950"
                li.innerHTML = `<h2 class="text-2xl font-bold text-white">Add a link to get started!</h2>`
                list.appendChild(li)
            }
        })
        .catch((error) => console.error("Fetch error:", error));
}

function getLinksTop() {
    fetch("/api/topFiveClicks").then((response) => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error("Uhoh cant get links");
        }
    })
        .then((data) => {
            if (data.length > 0) {
                showLinks(data);
            } else {
                let list = document.getElementById("listOfLinks")
                let li = document.createElement("li");
                li.className = "bg-stone-950"
                li.innerHTML = `<h2 class="text-2xl font-bold text-white">Add a link to get started!</h2>`
                list.appendChild(li)
            }
        })
        .catch((error) => console.error("Fetch error:", error));
}

function getLinkData(linkId) {
    fetch(`/api/getLinkData/${linkId}`)
        .then((response) => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error("Uhoh cant get link data");
            }
        })
        .then((data) => {
            editLink(data)
        })
        .catch((error) => console.error("Fetch error:", error));
}

function showLinks(data) {
    let list = document.getElementById("listOfLinks");
    const current_url = window.location.pathname
    console.log(current_url)
    for (i = 0; i < data.length; i++) {
        let li = document.createElement("li");
        li.className = "bg-stone-950 rounded-2xl w-full";
        if (data[i].tag != null) {
            li.innerHTML = `
                <div class="flex flex-row">
                    <a href="${data[i].link}" target="_blank" class="w-full p-3" onClick="updateLinkClick(${data[i].id})">
                        <div class="flex-col flex">
                            <h2 class='text-2xl font-extrabold text-white'>${data[i].title}</h2>
                            <h3 class="text-white opacity-80 font-bold">${data[i].tag}</h3>
                        </div>
                    </a>
                    <div class="flex flex-col justify-end p-2 gap-2">
                        <form method="post" action="/api/deleteLink">
                            <input type="hidden" name="id" value="${data[i].id}">
                            <input type="hidden" name="url" value="${current_url}">
                            <button type="submit" class="hover:cursor-pointer">
                                <img src="/static/svg/deleteDark.svg" alt="Delete SVG" class="size-6">
                            </button>
                        </form>
                            <button class="hover:cursor-pointer" onClick="getLinkData(${data[i].id})">
                                <img src="/static/svg/editDark.svg" alt="Edit SVG" class="size-6">
                            </button>
                    </div>
                </div>
            `;
        } else {
            li.innerHTML = `
                <div class="flex flex-row">
                    <a href="${data[i].link}" target="_blank" class="w-full p-3" onClick="updateLinkClick(${data[i].id})">
                        <input type="hidden" name="id" value="${data[i].id}">
                        <div class="flex-col flex">
                            <h2 class='text-2xl font-extrabold text-white'>${data[i].title}</h2>
                            <h3 class="text-white opacity-80 font-bold">(No Tag)</h3>
                        </div>
                    </a>
                    <div class="flex flex-col justify-end p-2 gap-2">
                        <form method="post" action="/api/deleteLink">
                            <input type="hidden" name="id" value="${data[i].id}">
                            <input type="hidden" name="url" value="${current_url}">
                            <button type="submit" class="hover:cursor-pointer">
                                <img src="/static/svg/deleteDark.svg" alt="Delete SVG" class="size-6">
                            </button>
                        </form>
                            <button class="hover:cursor-pointer" onClick="getLinkData(${data[i].id})">
                                <img src="/static/svg/editDark.svg" alt="Edit SVG" class="size-6">
                            </button>
                    </div>
                </div>
            `;
        }
        list.appendChild(li);
    }
}

function addLink() {
    const form = document.getElementById("newLinkForm");
    const links = document.getElementById("listOfLinks")
    if (form.classList.contains("hidden")) {
        form.classList.remove("hidden");
        links.classList.add("pointer-events-none")
        form.querySelector("form").reset();
    }
}

function cancelAddLink() {
    const form = document.getElementById("newLinkForm");
    const links = document.getElementById("listOfLinks")
    form.classList.add("hidden");
    links.classList.remove("pointer-events-none")
}

function editLink(data) {
    console.log("your here")
    const editDiv = document.getElementById("editLinkForm");
    const links = document.getElementById("listOfLinks") || document.getElementById("searchListResults")

    if (editDiv.classList.contains("hidden")) {
        editDiv.classList.remove("hidden");
        links.classList.add("pointer-events-none")
        editDiv.querySelector("form").reset();
        document.getElementById("editID").value = data[0]
        document.getElementById("editTitle").value = data[1]
        document.getElementById("editLink").value = data[2]
        document.getElementById("editTag").value = data[3]

    }
}

function cancelEditLink() {
    const form = document.getElementById("editLinkForm");
    const links = document.getElementById("listOfLinks")
    form.classList.add("hidden");
    links.classList.remove("pointer-events-none")
}

function updateLinkClick(linkId) {
    fetch(`/api/updateLinkClick`, {
        method: "POST", body: JSON.stringify({
            id: linkId
        }), headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    })
}







