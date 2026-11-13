ScriptHost:LoadScript("scripts/autotracking/item_mapping.lua")
ScriptHost:LoadScript("scripts/autotracking/location_mapping.lua")
ScriptHost:LoadScript("scripts/autotracking/tab_mapping.lua")

LEVEL_UNLOCKS = {}



CUR_INDEX = -1
SLOT_DATA = nil


function onClear(slot_data)
    SLOT_DATA = slot_data
    CUR_INDEX = -1

    for _, v in pairs(ITEM_MAPPING) do
        if v[1] then
            local obj = Tracker:FindObjectForCode(v[1])
            if obj then
                if v[2] == "toggle" then
                    obj.Active = false
                elseif v[2] == "progressive" then
                    if obj.Active then
                        obj.CurrentStage = 0
                    --else
                    --    obj.Active = true
                    end
                elseif v[2] == "consumable" then
                    obj.AcquiredCount = 0
                end
            end
        end
    end

    PLAYER_ID = Archipelago.PlayerNumber or -1
    TEAM_NUMBER = Archipelago.TeamNumber or 0

    if SLOT_DATA == nil then
        return
    end

    local fur_step_island = Tracker:FindObjectForCode("unlock_fur_step_island")
    fur_step_island.Active = true

    for i, j in pairs(slot_data) do
        print(tostring(i)..": "..tostring(j))
    end
end

function onItem(index, item_id, item_name, player_number)
    if index <= CUR_INDEX then return end
    local is_local = player_number == Archipelago.PlayerNumber
    CUR_INDEX = index;
    
    local v = ITEM_MAPPING[item_id]
    if not v then
        return
    end

    if not v[1] then
        return
    end

    local obj = Tracker:FindObjectForCode(v[1])
    if obj then
        if v[2] == "toggle" then
            obj.Active = true
        elseif v[2] == "progressive" then
            if obj.Active then
                obj.CurrentStage = obj.CurrentStage + 1
            else
                obj.Active = true
            end
        elseif v[2] == "consumable" then
            obj.AcquiredCount = obj.AcquiredCount + obj.Increment
        end
    end
end

function onLocation(location_id, location_name)
    local location_array = LOCATION_MAPPING[location_id]
    if not location_array or not location_array[1] then
        print(string.format("onLocation: could not find location mapping for id %s", location_id))
        return
    end

    for _, location in pairs(location_array) do
        local obj = Tracker:FindObjectForCode(location)
        if obj then
            if location:sub(1,1) == "@" then
                obj.AvailableChestCount = obj.AvailableChestCount - 1 
            else
                obj.Active = true
            end
        else 
            print(string.format("onLocation: could not find object for code %s", location))
        end
    end
end

function onNotify(key, value, old_value)
    updateEvents(key, value)
end

function onNotifyLaunch(key, value)
    updateEvents(key, value)
end

function updateEvents(key, value)
    print(key)
    if value ~= nil then
        if string.find(key, "smw_curlevelid_") then
            print(string.format("updateEvents %x",value))
            local tabswitch = Tracker:FindObjectForCode("tab_switch")
            Tracker:FindObjectForCode("cur_level_id").CurrentStage = value
            if tabswitch.Active then
                if TAB_MAPPING[value] then
                    CURRENT_ROOM = TAB_MAPPING[value]
                    for str in string.gmatch(CURRENT_ROOM, "([^/]+)") do
                        print(string.format("Updating ID %x to Tab %s",value,str))
                        Tracker:UiHint("ActivateTab", str)
                    end
                    print(string.format("Updating ID %x to Tab %s",value,CURRENT_ROOM))
                else
                    --CURRENT_ROOM = TAB_MAPPING[0x00]
                    print(string.format("Failed to find ID %x",value))
                    --Tracker:UiHint("ActivateTab", CURRENT_ROOM)
                end
            end
        elseif string.find(key, "smw_visitedlevels_") then
            --print(string.format("updateEvents %x",value))
            for _, level_id in ipairs(value) do
                level_visit = Tracker:FindObjectForCode("level_visit_" .. level_id)
                if level_visit ~= nil and not level_visit.Active then
                    level_visit.Active = 1
                    print("Setting level_visit_" .. level_id)
                end
            end
        end
    end
end


Archipelago:AddClearHandler("clear handler", onClear)
Archipelago:AddItemHandler("item handler", onItem)
Archipelago:AddLocationHandler("location handler", onLocation)
Archipelago:AddSetReplyHandler("notify handler", onNotify)
Archipelago:AddRetrievedHandler("notify launch handler", onNotifyLaunch)
