<script>
	import { Meta, Story, Template } from '@storybook/addon-svelte-csf';

	import Button from './Button.svelte';

	let count = 0;
	function handleClick() {
		count += 1;
	}
</script>

<Meta component={Button} autodocs />

<Template let:args>
	<Button {...args} on:click={handleClick} on:click>
		You clicked: {count}
	</Button>
</Template>

<Story name="Default" />

<Story name="Large" args={{ size: 'lg' }} />

<Story name="Small" source args={{ size: 'sm' }} />
