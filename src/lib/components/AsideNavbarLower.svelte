<script lang="ts">
	import { page } from '$app/stores';
	import * as Tooltip from '$lib/components/ui/tooltip/index.js';
	import { Settings } from 'lucide-svelte/icons';

	const settingsItem = { href: '/profile', icon: Settings, label: 'Settings' };

	$: activeItem = $page.url.pathname.split('/')[1] || 'dashboard';
</script>

<nav class="mt-auto flex flex-col items-center gap-4 px-2 py-4">
	<Tooltip.Root>
		<Tooltip.Trigger asChild let:builder>
			<a
				href={settingsItem.href}
				class="flex h-9 w-9 items-center justify-center rounded-lg text-muted-foreground transition-colors hover:text-foreground md:h-8 md:w-8 {activeItem ===
				settingsItem.href.slice(1)
					? 'bg-accent text-accent-foreground'
					: ''}"
				use:builder.action
				{...builder}
			>
				<svelte:component this={settingsItem.icon} class="h-5 w-5" />
				<span class="sr-only">{settingsItem.label}</span>
			</a>
		</Tooltip.Trigger>
		<Tooltip.Content side="right">{settingsItem.label}</Tooltip.Content>
	</Tooltip.Root>
</nav>
