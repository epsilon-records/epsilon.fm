<script lang="ts">
	import { superForm } from "sveltekit-superforms";
	import {
		Field,
		Control,
		Label,
		Description,
		FieldErrors,
		Fieldset,
		Legend,
	} from "formsnap";
    import { DateField,Button, SelectField, TextField } from "svelte-ux"
	import { zodClient } from "sveltekit-superforms/adapters";
	import type { PageData } from "./$types.js";
	import { allergies, schema, themes } from "./schema.js";
	import SuperDebug from "sveltekit-superforms";
 
	export let data: PageData;
 
	const form = superForm(data.form, {
		validators: zodClient(schema),
	});
	const { form: formData, enhance } = form;
</script>

<main class="p-2 grid place-items-center content-center">
    <form use:enhance class="mx-auto flex max-w-md flex-col" method="POST">
        <div class="grid grid-flow-col gap-2">
            <TextField label="First Name" placeholder="Please enter your first name" hint="Correct capitalization required" /> 
            <TextField label="Last Name" placeholder="Please enter your last name" hint="Correct capitalization required" />
        </div>
          <div class="grid grid-flow-col gap-2"><TextField
    label="Email"
    type="email"
    on:change={(e) => console.log(e.detail)}
  /></div>
  <div class="grid grid-flow-col gap-2"><DateField
  label="Birth date"
  on:change={(e) => (value = e.detail.value)}
  picker
  clearable
/></div>
        <Field {form} name="email">
            <Control let:attrs>
                <Label>Email</Label>
                <TextField {...attrs} type="email" bind:value={$formData.email} />
            </Control>
            <Description>Company email is preferred</Description>
            <FieldErrors />
        </Field>
        <Field {form} name="bio">
            <Control let:attrs>
                <Label>Bio</Label>
                <TextField multiline {...attrs} bind:value={$formData.bio} />
            </Control>
            <Description>Tell us a bit about yourself.</Description>
            <FieldErrors />
        </Field>
        <Field {form} name="language">
            <Control let:attrs>
                <Label>Language</Label>
                <SelectField {...attrs} bind:value={$formData.language}>
                    <option value="fr">French</option>
                    <option value="es">Spanish</option>
                    <option value="en">English</option>
                </SelectField>
            </Control>
            <Description>Help us address you properly.</Description>
            <FieldErrors />
        </Field>
        <Fieldset {form} name="theme">
            <Legend>Select your theme</Legend>
            {#each themes as theme}
                <Control let:attrs>
                    <Label>{theme}</Label>
                    <TextField {...attrs} type="radio" value={theme} bind:group={$formData.theme} />
                </Control>
            {/each}
            <Description>We prefer dark mode, but the choice is yours.</Description>
            <FieldErrors />
        </Fieldset>
        <Field {form} name="marketingEmails">
            <Control let:attrs>
                <TextField {...attrs} type="checkbox" bind:checked={$formData.marketingEmails} />
                <Label>I want to receive marketing emails</Label>
            </Control>
            <Description>Stay up to date with our latest news and offers.</Description>
            <FieldErrors />
        </Field>
        <Fieldset {form} name="allergies">
            <Legend>Food allergies</Legend>
            {#each allergies as allergy}
                <Control let:attrs>
                    <SelectField
                        {...attrs}
                        type="checkbox"
                        bind:group={$formData.allergies}
                        value={allergy}
                    />
                    <Label>{allergy}</Label>
                </Control>
            {/each}
            <Description>When we provide lunch, we'll accommodate your needs.</Description>
            <FieldErrors />
        </Fieldset>
        <Button>Submit</Button>
    </form> 
    <SuperDebug data={$formData} />
</main>