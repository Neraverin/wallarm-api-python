from pydantic import BaseModel
from typing import Any
from typing import List, Dict


class Feature(BaseModel):
    id: int
    slug: str


class Setting(BaseModel):
    name: str
    value: Any


class Binding(BaseModel):
    binding_id: int
    feature: Feature
    settings: List[Setting] = []


class Plan(BaseModel):
    id: int
    slug: str
    features: List[Feature] = []


class PlanElement(BaseModel):
    id: int
    slug: str
    use_features: bool
    features: List[Binding] = []


class Subscription(BaseModel):
    id: int
    client_id: int
    plan_id: int
    type: str
    state: str
    start_on: str
    finish_on: str
    position: str = None
    properties: Dict = None
    features: List[Binding]


class PartnerSettings(BaseModel):
    partner_id: int = None
    trial_plan_slug: str = None
    trial_period: int = None
    trial_extend_period: int = None
    trial_wait_period: int = None
    trials_enabled: bool
