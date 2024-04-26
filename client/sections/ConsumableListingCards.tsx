import { fetchConsumables } from "@/app/consumable/fetchConsumables";
import wrapPromise from "@/app/utils/wrapPromise";
import ConsumableCard from "@/components/Consumables/ConsumableCard";

const res = wrapPromise(fetchConsumables());
const API_URL = process.env.NEXT_PUBLIC_API_URL;

export default async function ConsumableListingCards() {
  const consumables = res.read();

  return (
    <div className="flex flex-wrap justify-center content-start gap-10 w-full">
      {consumables &&
        consumables.map((consumable: any) => {
          return (
            <ConsumableCard
              key={consumable.id}
              image={`${API_URL}/${consumable.image_path}`}
              name={consumable.name}
              type={consumable.type}
            />
          );
        })}
    </div>
  );
}
