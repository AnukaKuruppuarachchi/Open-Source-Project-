#pragma once
#include <cstdint>
#include "game/organization/special_flavour_id_types.h"
#include "game/detail/inventory/requested_equipment.h"
#include "game/enums/marker_type.h"
#include "game/enums/faction_type.h"

struct bomb_defusal_rules {
	// GEN INTROSPECTOR struct bomb_defusal_rules
	bool dummy = false;
	// END GEN INTROSPECTOR

	static constexpr bool has_economy() {
		return true;
	}

	static auto get_name() {
		return "Bomb Defusal";
	}
};

struct gun_game_rules {
	// GEN INTROSPECTOR struct gun_game_rules
	bool dummy = true;

	per_actual_faction<requested_equipment> basic_eq;
	per_actual_faction<requested_equipment> final_eq;

	std::vector<item_flavour_id> progression;
	bool can_throw_melee_on_final_level = true;
	// END GEN INTROSPECTOR

	int get_final_level() const {
		return static_cast<int>(progression.size());
	}

	static constexpr bool has_economy() {
		return false;
	}

	static auto get_name() {
		return "Gun Game";
	}
};

struct capture_the_flag_rules {
	// GEN INTROSPECTOR struct capture_the_flag_rules
	uint32_t score_to_win = 3;
	item_flavour_id flag_flavour;
	marker_letter_type resistance_base_letter = marker_letter_type::A;
	marker_letter_type metropolis_base_letter = marker_letter_type::B;
	// END GEN INTROSPECTOR

	static constexpr bool has_economy() {
		return false;
	}

	static auto get_name() {
		return "Capture The Flag";
	}

	marker_letter_type get_base_letter(const faction_type faction) const {
		if (faction == faction_type::RESISTANCE) {
			return resistance_base_letter;
		}

		return metropolis_base_letter;
	}
};

using all_subrules_variant = std::variant<
	bomb_defusal_rules,
	gun_game_rules,
	capture_the_flag_rules
>;
