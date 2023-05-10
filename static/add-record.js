for (let addMemberBtn of document.getElementsByClassName("addMemberBtn"))
{
    addMemberBtn.addEventListener("click", addAppMember);
}

function addAppMember(event)
{
    var elementTriggerer = event.currentTarget;

    if (elementTriggerer.previousSibling.previousSibling.value.trim().length < 1)
    {
        return;
    }

    var ul;

    if (elementTriggerer.parentElement.parentElement.children.length > 1)
    {
        ul = elementTriggerer.parentElement.parentElement.children[0];

        let li = document.createElement("li");
        li.className = "spacingBetweenListItems";
        li.innerHTML = elementTriggerer.previousSibling.previousSibling.value;

        let deleteBtn = document.createElement("button");
        deleteBtn.innerHTML = "X";
        deleteBtn.classList.add("generalBtn");
        deleteBtn.classList.add("deleteBtn");
        deleteBtn.addEventListener("click", deleteDetail);

        li.append(deleteBtn);

        ul.append(li);
    }
    else
    {
        ul = document.createElement("ul");
        ul.className = "multipleValuesList";

        let li = document.createElement("li");
        li.className = "spacingBetweenListItems";
        li.innerHTML = elementTriggerer.previousSibling.previousSibling.value;

        let deleteBtn = document.createElement("button");
        deleteBtn.innerHTML = "X";
        deleteBtn.classList.add("generalBtn");
        deleteBtn.classList.add("deleteBtn");
        deleteBtn.addEventListener("click", deleteDetail);

        li.append(deleteBtn);

        ul.append(li);

        let addingDiv = elementTriggerer.parentElement;
        let liParent = addingDiv.parentElement;

        elementTriggerer.parentElement.remove();

        liParent.append(ul);
        liParent.append(addingDiv);
    }
}

function deleteDetail(event)
{
    event.currentTarget.parentElement.remove();
    updateCompliancyStatus(event.currentTarget.parentElement.parentElement.parentElement.children[2]);

}

document.getElementsByTagName("select")[0].addEventListener("change", addComponent);

function addComponent(event)
{
    var elementTriggerer = event.currentTarget;

    if (elementTriggerer.previousSibling.previousSibling.value.trim().length < 1 || elementTriggerer.value == "0")
    {
        return;
    }

    if (elementTriggerer.parentElement.parentElement.children.length > 1)
    {
        ul = elementTriggerer.parentElement.parentElement.children[0];

        let li = document.createElement("li");
        li.className = "spacingBetweenListItems";
        li.innerHTML = elementTriggerer.previousSibling.previousSibling.value;

        let label = document.createElement("label");

        switch (elementTriggerer.value)
        {
            case "1":
                label.innerHTML = "Compliant";
                label.className = "greenColor";
                break;
            case "2":
                label.innerHTML = "Non-Compliant";
                label.className = "redColor";
                break;
        }

        label.classList.add("spaceOnTheLeft");

        let deleteBtn = document.createElement("button");
        deleteBtn.innerHTML = "X";
        deleteBtn.classList.add("generalBtn");
        deleteBtn.classList.add("deleteBtn");
        deleteBtn.addEventListener("click", deleteDetail);

        li.append(label);
        li.append(deleteBtn);

        ul.append(li);
    }
    else
    {
        ul = document.createElement("ul");
        ul.className = "multipleValuesList";

        let li = document.createElement("li");
        li.className = "spacingBetweenListItems";
        li.innerHTML = elementTriggerer.previousSibling.previousSibling.value;

        let label = document.createElement("label");

        switch (elementTriggerer.value)
        {
            case "1":
                label.innerHTML = "Compliant";
                label.className = "greenColor";
                break;
            case "2":
                label.innerHTML = "Non-Compliant";
                label.className = "redColor";
                break;
        }

        label.classList.add("spaceOnTheLeft");

        let deleteBtn = document.createElement("button");
        deleteBtn.innerHTML = "X";
        deleteBtn.classList.add("generalBtn");
        deleteBtn.classList.add("deleteBtn");
        deleteBtn.addEventListener("click", deleteDetail);

        li.append(label);
        li.append(deleteBtn);

        ul.append(li);

        let addingDiv = elementTriggerer.parentElement;
        let liParent = addingDiv.parentElement;

        elementTriggerer.parentElement.remove();

        liParent.append(ul);
        liParent.append(addingDiv);
    }

    elementTriggerer.removeEventListener("change", addComponent);

    elementTriggerer.value = "0";

    elementTriggerer.addEventListener("change", addComponent);

    updateCompliancyStatus(elementTriggerer);
}

function updateCompliancyStatus(elementTriggerer)
{
    var compliancyLabel = document.getElementsByClassName("compliancyLabel")[0];

    for (let component of elementTriggerer.parentElement.parentElement.children[0].children)
    {
        if (component.children[0].innerHTML == "Non-Compliant")
        {
            compliancyLabel.innerHTML = "Non-Compliant";
            compliancyLabel.classList.add("redColor");
            return;
        }
    }

    compliancyLabel.innerHTML = "Compliant";
    compliancyLabel.classList.add("greenColor");
}
