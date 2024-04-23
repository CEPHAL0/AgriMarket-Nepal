import ConsumableCard from "@/components/Consumables/ConsumableCard";

export default function Page() {
  return (
    <ConsumableCard
      image="test.png"
      name="Radish"
      type={ConsumableType.Fruit}
    />
  );
}
