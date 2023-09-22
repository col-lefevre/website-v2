import csv

def getProjectData(idNum):
    projects = researchDataParse()
    for project in projects:
        if int(project["id"]) == int(idNum):
            return project
        
def getProjectSummaries():
    projectList = []
    projects = researchDataParse()
    for project in projects:
        projectList.append({"id": project["id"], "stub": project["stub"], "blurb": project["blurb"]})

    return projectList

def researchDataParse():
    dataList = []

    # Main.csv
    with open("pyData/research/main.csv", mode="r", newline="") as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            dataList.append(row)

    # Text.csv
    with open("pyData/research/text.csv", mode="r", newline="") as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            dataListId = int(row["id"])-1
            if "text" not in dataList[dataListId].keys():
                dataList[dataListId]["text"] = [row["body"]]
            else:
                dataList[dataListId]["text"].append(row["body"])

    # Buttons.csv
    with open("pyData/research/buttons.csv", mode="r", newline="") as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            dataListId = int(row["id"])-1
            if "buttons" not in dataList[dataListId].keys():
                dataList[dataListId]["buttons"] = [{"title": row["title"], "link": row["link"] }]
            else:
                dataList[dataListId]["buttons"].append({"title": row["title"], "link": row["link"] })

    # Details.csv
    with open("pyData/research/details.csv", mode="r", newline="") as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            dataListId = int(row["id"])-1
            if "details" not in dataList[dataListId].keys():
                dataList[dataListId]["details"] = [{"title": row["title"], "body": row["body"] }]
            else:
                dataList[dataListId]["details"].append({"title": row["title"], "body": row["body"] })

    return dataList

# print(getProjectSummaries())