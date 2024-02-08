from aiogram.fsm.state import StatesGroup, State

class NewDreamState(StatesGroup):
    enter_date = State()
    enter_sussy_date = State()
    enter_dream = State()
    enter_sleep_type = State()
    enter_location = State()
    enter_feelings = State()
    enter_vision = State()
    enter_subjective_sleep_duration = State()
    enter_sleep_start = State()
    enter_sleep_end = State()
    enter_dream_type = State()
    confirm = State()

