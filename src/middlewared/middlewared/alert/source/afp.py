from middlewared.alert.base import AlertClass, AlertCategory, AlertLevel, OneShotAlertClass, Alert


class AFPShareLockedAlertClass(AlertClass, OneShotAlertClass):
    deleted_automatically = False

    category = AlertCategory.SHARING
    level = AlertLevel.WARNING
    title = 'AFP Share Locked'
    text = 'AFP "%(name)s" share operating on a locked resource. Please disable the share.'

    async def create(self, args):
        return Alert(AFPShareLockedAlertClass, args, key=args['id'])

    async def delete(self, alerts, query):
        return list(filter(
            lambda alert: alert.key != str(query),
            alerts
        ))