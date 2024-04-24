import { BookedEnumType, ConsumableType } from "@/app/lib/definitions";
// import { StaticImageData } from "next/image";
import Image from "next/image";
import { typeClassMap } from "@/app/lib/definitions";
import LocationSign from "@/public/LocationSign";
import { Consumable, User } from "@/types/types";

interface SurplusListingCardProps {
  price: number;
  booked: BookedEnumType;
  farmer: User;
  consumable: Consumable;
}

export default function SurplusListingCard(props: SurplusListingCardProps) {
  const image_src = `${process.env.NEXT_PUBLIC_API_URL}/${props.consumable.image_path}`;
  const image_src_user = `${process.env.NEXT_PUBLIC_API_URL}/${props.farmer.image}`;

  return (
    <div className="relative inline-block">
      <div
        className={`h-80 w-64 rounded-xl flex flex-col shadow-md shadow-primary-gray ${
          typeClassMap[props.consumable.type]
        }`}
      >
        {/* Add text with background indicating whether it is booked or not */}
        <div className="absolute top-2 right-2 bg-black text-white py-1 px-2 rounded-md z-40">
          {props.booked === "BOOKED" ? "Booked" : "Not Booked"}
        </div>

        <div className="h-[50%] relative w-full">
          <Image src={image_src} alt="name" priority={true} className="object-cover rounded-t-xl" fill />
        </div>
        <div className="flex flex-col items-start justify-between p-4 grow gap-4">
          <div className="flex flex-col gap-2">
            {/* User Information Section */}
            <div className="flex gap-1">
              <div className="relative h-5 w-5 rounded-full border border-black">
                <Image src={image_src_user} fill className="object-cover rounded-full" alt={props.farmer.name} />
              </div>
              <p className="text-sm truncate max-w-24">{props.farmer.name}</p>
            </div>

            <div className="flex gap-2 ">
              <LocationSign />
              <p className="text-xs truncate max-w-24 text-gray-500">{props.farmer.address}</p>
            </div>
          </div>

          <div className="flex items-center justify-between w-full">
            <p className=" font-semibold text-3xl text-primary-blue">{props.consumable.name}</p>
            <span className="bg-black w-fit h-fit rounded-xl px-2 py-1 text-xs text-white">
              {props.consumable.type.toUpperCase()}
            </span>
          </div>

          <div className="flex justify-between w-full items-start">
            <div className="text-xl text-gray-700 font-[600]">
              Rs.{props.price}
              <span className="text-xs">/kg</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
