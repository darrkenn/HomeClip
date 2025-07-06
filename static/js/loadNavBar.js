function loadNavBar() {
    let body = document.body
    let desktopNav = document.createElement("div")
    let mobileNav = document.createElement("div")
    desktopNav.className = "w-1/6 bg-nice-footer h-full hidden md:flex md:flex-col gap-4 items-center"
    desktopNav.innerHTML = `
        <a href="/">
        <h1 class="text-center text-white text-4xl pt-4 font-extrabold">HomeClip</h1>
    </a>
    <div class="bg-amber-300  flex flex-col items-center justify-center">
        <form id="searchForm" method="dialog" onsubmit="navigateSearch()" onkeyup="updateAndRetrievePreviewSearchBox()" autocomplete="off" >
            <input class="bg-white p-1 outline-0" id="searchValue" type="text" name="searchValue" placeholder="Search:">
        </form>
        <ul id="searchList" class=" flex-col gap-2 items-center text-black bg-white w-full hidden"></ul>
    </div>
    `
    mobileNav.className = "min-h-1/12 bg-nice-footer w-full flex flex-row md:hidden items-center"
    mobileNav.innerHTML = `
    <a href="/">
        <h1 class="text-left pl-4 text-white text-3xl font-extrabold hover:cursor-pointer">HomeClip</h1>
    </a>
    `
    body.prepend(desktopNav)
    body.prepend(mobileNav)


}