import { BookedEnumType, ConsumableType, RoleEnumType } from "@/app/lib/definitions";

type Link = {
  name: string;
  path: string;
};

type Consumable = {
  id?: int;
  name: string;
  type: ConsumableType;
  image_path: string;
  created_at: Date;
  updated_at: Date;
};

type User = {
  id?: int;
  name: string;
  username: string;
  email: string;
  image: string;
  role: RoleEnumType;
  address: string;
  phone: string;
  created_at: Date;
  updated_at: Date;
};

type SurplusListing = {
  id: number;
  consumable_id: number;
  price: number;
  booked: BookedEnumType;
  farmer_id: number;
  farmer: User;
  consumable: Consumable;
  created_at: Date;
  updated_at: Date;
};
