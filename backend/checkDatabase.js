import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

async function main() {
    
    const user = await prisma.teacherAssist.findMany();
    console.log(user);
}

main();