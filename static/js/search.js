function updateAndRetrievePreviewSearchBox() {
    let list = document.getElementById("searchList")
    let sV = document.getElementById("searchValue").value;
    if (list.classList.contains("hidden")) {
        list.classList.remove("hidden")
    }
    if (sV.length > 0) {
        if (sV.match(/tag:.*/)) {
            let tagValue = `tag=${sV.slice(5)}`
            retrievePreviewSearchListValue(tagValue)
        } else if (sV.match(/folder:.*/)) {
            let folderValue = `folder=${sV.slice(8)}`
            console.log(folderValue)
            retrievePreviewSearchListValue(folderValue)
        } else {
            let titleValue = `title=${sV}`
            retrievePreviewSearchListValue(titleValue)
        }
    }
    if (sV.length === 0) {
        list.classList.add("hidden")
        list.innerHTML = ""
    } else if (sV === "tag: " || sV === "folder: ") {
        list.classList.add("hidden")
        list.innerHTML = ""
    }
}

function retrievePreviewSearchListValue(value) {
    fetch(`/api/getSearchResults/preview/${value}`)
        .then((response) => {
            if (response.ok) {
                return response.json()
            } else {
                throw new Error("uhoh")
            }
        })
        .then((data) => {
            let splitArray = value.split("=")
            if (splitArray[0] === "title") {
                updateSearchList(data, "title")
            } else if (splitArray[0] === "tag") {
                updateSearchList(data, "tag")
            } else if (splitArray[0] === "folder") {
                updateSearchList(data, "folder")
            }
        })
}


function updateSearchList(data, type) {
    let list = document.getElementById("searchList")
    let sV = document.getElementById("searchValue")
    list.innerHTML = ""
    for (let i=0; i < data.length; i++) {
        let li = document.createElement("li");
        li.className = "w-full p-0.5";
        if (type === "title") {
            li.innerHTML = `
                    <a href="${data[i][1]}" target="_blank">
                    <h1>${data[i][0]}</h1>
                    </a>
        `;
        } else if (type === "tag") {
            li.innerHTML = `
                    <a target="_blank">
                    <h1>${data[i][0]}</h1>
                    </a>
        `;
        } else if (type === "folder") {
            li.innerHTML = `
                    <a target="_blank">
                    <h1>${data[i][0]}</h1>
                    </a>
        `;
        }
        list.appendChild(li)
    }
}

function navigateSearch() {
    let sV = document.getElementById("searchValue").value;
    console.log("test")
    if (sV.length > 0) {
        if (sV.match(/tag:.*/)) {
            window.location.replace(`search?type=tag&tag=${sV.slice(5)}`)
        } else if (sV.match(/folder:.*/)) {
            window.location.replace(`search?type=folder&folder=${sV.slice(8)}`)
        } else {
            window.location.replace(`search?type=title&title=${sV}`)
        }
    }
    else {
        window.location.replace("search")
    }
}
function navigateBigSearch() {
    let bSV = document.getElementById("bigSearchValue").value;
    console.log(bSV)
    if (bSV.length > 0) {
        if (bSV.match(/tag:.*/)) {
            window.location.replace(`search?type=tag&tag=${bSV.slice(5)}`)
        } else if (bSV.match(/folder:.*/)) {
            window.location.replace(`search?type=folder&folder=${bSV.slice(8)}`)
        } else {
            window.location.replace(`search?type=title&title=${bSV}`)
        }
    }
    else {
        window.location.replace("search")
    }
}

function retrieveBigSearchValues(type, value) {
    fetch(`/api/getSearchResults/full/${type}=${value}`)
        .then((result) => {
            if (result.ok) {
                return result.json()
            } else{
                throw new Error("whoops")
            }
        })
        .then ((data) => {
            showBigSearchValues(data)
        })
}

function showBigSearchValues(data) {
    let typeOfData = Object.keys(data).toString()
    if (typeOfData === "titles") {
        const values = data.titles
        console.log(values)
        searchListUpdate(values, typeOfData)
    } else if (typeOfData === "tags") {
        const values = data.tags
        console.log(values)
        searchListUpdate(values, typeOfData)
    } else if (typeOfData === "folders") {
        const values = data.folders
        console.log(values)
        searchListUpdate(values, typeOfData)
    }
}

function searchListUpdate(values, typeOfData) {
    let list = document.getElementById("searchListResults");
    if (values.length > 0) {
        if (typeOfData === "tags" || typeOfData === "folders") {
            list.classList.remove("flex-col")
            list.classList.add("flex-row", "space-evenly", "flex-wrap")
        }

        for (let i = 0; i < values.length; i++) {
            let li = document.createElement("li")
            if (typeOfData === "titles") {
                li.className = "bg-stone-950 rounded-2xl w-full"
                li.innerHTML = `
                    <div class="flex flex-row ">
                        <a href="${values[i].link}" target="_blank" class="w-full p-3" onClick="updateLinkClick(${values[i].id})">
                            <div class="flex-col flex">
                                <h2 class='text-2xl font-extrabold text-white'>${values[i].title}</h2>
                                <h3 class="text-white opacity-80 font-bold">${values[i].tag}</h3>
                            </div>
                        </a>
                        <div class="flex flex-col justify-end p-2 gap-2">
                            <form method="post" action="/api/deleteLink">
                                <input type="hidden" name="id" value="${values[i].id}">
                                <input type="hidden" name="url" value="${window.location.href}">
                                <button type="submit" class="hover:cursor-pointer">
                                    <img src="/static/svg/deleteDark.svg" alt="Delete SVG" class="size-6">
                                </button>
                            </form>
                                <button class="hover:cursor-pointer" onClick="getLinkData(${values[i].id})">
                                    <img src="/static/svg/editDark.svg" alt="Edit SVG" class="size-6">
                                </button>
                        </div>
                    </div>
            
                `
            } else if (typeOfData === "tags" || typeOfData === "folders") {
                li.className = "bg-stone-950 rounded-2xl min-w-1/4 max-w-1/4 text-center size-12"
                li.innerHTML = `
                    <a class="hover:cursor-pointer w-full h-full bg-nice-footer rounded-2xl flex items-center justify-center">
                    <h1 class="text-lg text-white font-bold">${values[i]}</h1>
                    </a>
                    
                `
            }
            list.appendChild(li);
        }
    } else {
        let li = document.createElement("li")
        li.className = "w-full text-center"
        li.innerHTML = `<h1 class="text-5xl text-white font-bold">NO VALUES</h1>`
        list.appendChild(li)
    }
}

