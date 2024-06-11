import { BookedType, ConsumableType, RoleType } from "@/app/lib/definitions";

type Link = {
  name: string;
  path: string;
};

type Consumable = {
  id?: int;
  name: string;
  type: ConsumableType;
  image_path: string;
  created_at: string;
  updated_at: string;
};

type User = {
  id?: int;
  name: string;
  username: string;
  email: string;
  image: string;
  role: RoleType;
  address: string;
  phone: string;
  created_at: string;
  updated_at: string;
};

type SurplusListing = {
  id: number;
  consumable_id: number;
  price: number;
  booked: BookedType;
  farmer_id: number;
  farmer: User;
  consumable: Consumable;
  created_at: string;
  updated_at: string;
};
