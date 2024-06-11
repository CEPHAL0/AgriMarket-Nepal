import { ReactElement } from "react";
import { ConsumableType } from "@/app/lib/definitions";
import Image, { StaticImageData } from "next/image";
export default function ConsumableCard({
  name,
  type,
  image,
}: {
  name: string;
  type: ConsumableType;
  image: StaticImageData | string;
}): ReactElement {
  const typeClassMap = {
    FRUIT: "bg-fruit",
    VEGETABLE: "bg-vegetable",
    OTHER: "bg-other",
  };

  return (
    <div
      className={`h-72 w-64 rounded-xl flex flex-col shadow-md shadow-primary-gray ${typeClassMap[type]}`}
    >
      <div className="h-[70%] relative w-full">
        <Image
          src={image}
          alt="name"
          priority={true}
          className="object-cover rounded-t-xl"
          fill
        />
      </div>
      <div className="flex items-center justify-between p-4 grow">
        <p className="font-semibold text-2xl text-primary-blue">{name}</p>
        <span className="bg-black w-fit h-fit rounded-xl px-2 py-1 text-[0.6rem] text-white">
          {type.toUpperCase()}
        </span>
      </div>
    </div>
  );
}
