import ConsumableCard from "@/components/Consumables/ConsumableCard";
import Vegetable from "@/public/Vegetables.jpg";
export default function Page() {
  return (
    <div className="m-6 flex gap-4">
      <ConsumableCard image={Vegetable} name="Radish" type="VEGETABLE" />
      <ConsumableCard image={Vegetable} name="Apple" type="FRUIT" />
      <ConsumableCard image={Vegetable} name="Milk" type="OTHER" />
    </div>
  );
}
