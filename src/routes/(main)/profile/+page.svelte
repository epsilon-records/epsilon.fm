<script lang="ts">
	import type { PageData } from './$types.js';
	import ProfileForm from '$lib/components/ProfileForm.svelte';
	import { Separator } from '$lib/components/ui/separator/index.js';

	export let data: PageData;
</script>

<div class="space-y-6">
	<div>
		<h3 class="text-lg font-medium">Profile</h3>
		<p class="text-sm text-muted-foreground">This is how others will see you on the site.</p>
	</div>
	<Separator />
	{#if data.form}
		<ProfileForm data={data.form} />
	{/if}
</div>
