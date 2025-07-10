function loadNavBar() {
    let body = document.body
    let desktopNav = document.createElement("div")
    desktopNav.className = "bg-nice-footer gap-4 items-center min-h-1/12 w-full flex flex-row md:w-1/6 bg-nice-footer md:h-full md:flex md:flex-col"
desktopNav.innerHTML = `
    <a href="/">
        <h1 class="text-left pl-4 md:pl-0 md:text-center w-full text-white text-3xl lg:text-4xl md:pt-4 font-extrabold">HomeClip</h1>
    </a>
    <div class="relative w-1/3 md:w-fit">
        <form id="searchForm" method="dialog" onsubmit="navigateSearch()" onkeyup="updateAndRetrievePreviewSearchBox()" autocomplete="off">
            <input class="bg-white p-1 outline-0 w-full" id="searchValue" type="text" name="searchValue" placeholder="Search:">
        </form>
        <ul id="searchList" class="absolute top-full left-0 right-0 bg-white mt-1 hidden"></ul>
    </div>
`;
    body.prepend(desktopNav)
}