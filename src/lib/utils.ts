export const serializeNonPOJO = (obj: any) => {
    return structuredClone(obj);
};