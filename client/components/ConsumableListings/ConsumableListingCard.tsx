import { ConsumableType } from "@/app/lib/definitions";
import { StaticImageData } from "next/image";
import Image from "next/image";
import { typeClassMap } from "@/app/lib/definitions";
import LocationSign from "@/public/LocationSign";

interface ConsumableListingCardProps {
  consumable: string;
  user: string;
  price: number;
  postedDate: string;
  district: string;
  quantity: number;
  expiryDate?: string;
  userImage: StaticImageData | string;
  consumableImage: StaticImageData | string;
  consumableType: ConsumableType;
}

export default function ConsumableListingCard(
  props: ConsumableListingCardProps
) {
  return (
    <div
      className={`h-96 w-64 rounded-xl flex flex-col shadow-md shadow-primary-gray ${
        typeClassMap[props.consumableType]
      }`}
    >
      <div className="h-[70%] relative w-full">
        <Image
          src={props.consumableImage}
          alt="name"
          priority={true}
          className="object-cover rounded-t-xl"
          fill
        />
      </div>
      <div className="flex flex-col items-start justify-between p-4 grow gap-4">
        <div className="flex flex-col gap-2">
          {/* User Information Section */}
          <div className="flex gap-1">
            <div className="relative h-5 w-5 rounded-full border border-black">
              <Image
                src={props.userImage}
                fill
                className="object-cover rounded-full overflow-hidden"
                alt={props.user}
              />
            </div>
            <p className="text-sm truncate max-w-24">{props.user}</p>
          </div>

          <div className="flex gap-2 ">
            <LocationSign />
            <p className="text-xs truncate max-w-24 text-gray-500">
              {props.district}
            </p>
          </div>
        </div>

        <div className="flex items-center justify-between w-full gap-3">
          <p className="w-2/3 font-semibold text-2xl text-primary-blue">
            {props.consumable}
          </p>
          <span className="bg-black w-fit h-fit rounded-xl px-2 py-1 text-xs text-white">
            {props.consumableType.toUpperCase()}
          </span>
        </div>

        <div className="flex justify-between w-full items-start">
          <div className="text-lg text-gray-700 font-[600]">
            Rs.{props.price}
            <span className="text-xs">/kg</span>
          </div>

          <div className="text-sm flex flex-col items-end">
            {props.quantity} Kg{" "}
            <span className="text-xs font-extralight">available</span>
          </div>
        </div>
      </div>
    </div>
  );
}
