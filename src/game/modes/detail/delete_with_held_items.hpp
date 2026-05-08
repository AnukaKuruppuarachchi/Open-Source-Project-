#pragma once
#include "game/messages/will_soon_be_deleted.h"
#include "game/detail/entity_handle_mixins/for_each_slot_and_item.hpp"
#include "game/detail/inventory/perform_transfer.h"

class arena_mode;

void reverse_perform_deletions(const deletion_queue& deletions, cosmos& cosm);

template <class H>
static void delete_with_held_items_except(const entity_flavour_id drop_instead, const entity_flavour_id drop_instead_second, const H handle) {
	if (handle) {
		deletion_queue q;
		q.push_back(handle.get_id());

		handle.for_each_contained_item_recursive(
			[&](const auto& contained) {
				if (drop_instead.is_set() || drop_instead_second.is_set()) {
					const auto this_flavour = entity_flavour_id(contained.get_flavour_id());

					if (
						drop_instead == this_flavour
						|| drop_instead_second == this_flavour
					) {
						/* Don't delete preserved objective items. Drop them instead. */

						auto request = item_slot_transfer_request::drop(contained);
						request.params.bypass_mounting_requirements = true;

						const auto result = perform_transfer_no_step(request, handle.get_cosmos());
						// Not required as there will never be any deletion involved.
						//result.notify_logical(step);
						(void)result;

						return;
					}
				}

				q.push_back(entity_id(contained.get_id()));
			}
		);

		if (auto sentience = handle.template find<components::sentience>()) {
			q.push_back(sentience->detached.head);
			q.push_back(sentience->detached.arm_upper);
			q.push_back(sentience->detached.arm_lower);
			q.push_back(sentience->detached.lying_corpse);
		}

		reverse_perform_deletions(q, handle.get_cosmos());
	}
}

template <class H>
static void delete_with_held_items_except(const entity_flavour_id drop_instead, const H handle) {
	::delete_with_held_items_except(drop_instead, entity_flavour_id(), handle);
}

