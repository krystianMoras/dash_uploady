import React from 'react';
import PropTypes from 'prop-types';
import { useBatchStartListener, useBatchFinishListener, useUploady } from '@rpldy/uploady';

const DashUploadyTarget = (props) => {


    const uploady = useUploady();

    const onClick = () => {
        uploady.showFileUpload();
    };

    return (
        <div {...props} onClick={onClick}>
            {props.children}
        </div>
    );
};

DashUploadyTarget.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks
     */
    id: PropTypes.string,

    /**
     * Children components
     */
    children: PropTypes.node
};

export default DashUploadyTarget;