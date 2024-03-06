import asyncio
import json


async def task_1():
    names, prices = await task_2()
    with open("task_2.json", "w")as file:
        json.dump(names,file, sort_keys=True, indent=2)
        json.dump(prices,file, sort_keys=True, indent=2)


async def task_2():
    with open('task_1.json', "r") as file:
        data = json.load(file)
        names = []
        prices = []
        for i in data["courses"]:
            names.append(i["names"])
            prices.append(i["price"])
        return names, prices

async def main():
    await task_1()

if __name__ == "__main__":
    asyncio.run(main())




