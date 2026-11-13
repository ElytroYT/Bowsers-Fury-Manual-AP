Tracker:AddItems("items/items.json")

local variant = Tracker.ActiveVariantUID

if variant == "standard" then
    Tracker:AddLayouts("layouts/items.json")
elseif variant == "no_power_up_abilities" then
    Tracker:AddLayouts("layouts/no_power_up_abilities.json")
end

ScriptHost:LoadScript("scripts/autotracking.lua")

Tracker:AddLayouts("layouts/tracker.json")

DEBUG = true