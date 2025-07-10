function loadEditLink() {
    let body = document.body
    let editForm = document.createElement("div")

    editForm.className = "fixed top-1/2 left-1/2 -translate-y-1/2 -translate-x-1/2 bg-nice-footer hidden border-3 rounded-2xl border-white p-2 transition-all pointer-events-auto z-50"
    editForm.id = "editLinkForm"
    editForm.innerHTML = `
            <div class="flex flex-row border-b-2 border-white w-full">
            <div class="w-1/2"><h1 class="text-white text-2xl font-extrabold">Edit Link</h1></div>
            <div class="w-1/2 justify-end flex">
                <button class="text-white text-lg p-1 font-bold hover:cursor-pointer" onclick="cancelEditLink()">
                    Cancel
                </button>
            </div>
        </div>
        <form method="post" action="/api/editLink" class="flex flex-col gap-2 pt-2" autocomplete="off">
            <div class="flex flex-row">
                <div class="flex flex-col w-1/4 gap-2 text-white font-bold">
                    <label class="p-0.5">Title:</label>
                    <label class="p-0.5">Link:</label>
                    <label class="p-0.5">Tag:</label>
                </div>
                <div class="flex flex-col w-full gap-2 text-black">
                    <input class="hidden" type="number" id="editID" name="id">
                    <input class="hidden" id="currentUrl" name="url" value="${window.location.pathname}">
                    <input class="bg-white p-0.5" id="editTitle" type="text" name="title" placeholder="Title" required/>
                    <input class="bg-white p-0.5" id="editLink" type="text" name="link" placeholder="Link"
                           pattern="https?://.+" required/>
                    <input class="bg-white p-0.5" id="editTag" type="text" name="tag" placeholder="Tag">
                </div>
            </div>
            <div class="flex flex-row items-center justify-center gap-1 w-full">
                <button type="submit" class="bg-white text-black font-bold rounded-2xl p-2 hover:cursor-pointer">
                    Submit
                </button>
            </div>
        </form>
    `
    body.appendChild(editForm)
}