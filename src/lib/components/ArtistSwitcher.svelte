<script lang="ts">
	import OrganizationSwitcher from 'clerk-sveltekit/client/OrganizationSwitcher.svelte';
	import { mode } from 'mode-watcher';
	import { neobrutalism, dark } from '@clerk/themes';
</script>

{#key $mode}
	<div class="pt-2">
		<OrganizationSwitcher
			appearance={{ baseTheme: $mode === 'dark' ? dark : neobrutalism }}
			hidePersonal={true}
			afterCreateOrganizationUrl="/profile"
			afterSelectOrganizationUrl="/profile"
		/>
	</div>
{/key}
