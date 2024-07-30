<script lang="ts">
	import * as Menubar from '$lib/components/ui/menubar/index.js';
	import { page } from '$app/stores';

	const items = [
		'profile',
		'profile/account',
		'profile/appearance',
		'profile/display',
		'profile/notifications'
	];

	function formatItemName(item: string): string {
		const parts = item.split('/');
		const lastPart = parts[parts.length - 1];
		return lastPart.charAt(0).toUpperCase() + lastPart.slice(1);
	}
</script>

<Menubar.Sub>
	<Menubar.SubTrigger inset>Settings</Menubar.SubTrigger>
	<Menubar.SubContent class="w-[230px]">
		<Menubar.RadioGroup value={$page.url.pathname}>
			{#each items as item}
				<a href="/{item}">
					<Menubar.RadioItem disabled={$page.url.pathname === `/${item}`} value={`/${item}`}>
						{formatItemName(item)}
					</Menubar.RadioItem>
				</a>
			{/each}
		</Menubar.RadioGroup>
	</Menubar.SubContent>
</Menubar.Sub>
